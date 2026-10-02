from dataclasses import dataclass
from datetime import datetime,timezone
from email.utils import parsedate_to_datetime
from urllib.request import Request,urlopen
import xml.etree.ElementTree as ET

@dataclass(frozen=True)
class RSSArticle:
    title:str
    source:str
    published_at:datetime
    url:str

class RSSNewsProvider:
    def __init__(self,timeout:float=10.0): self.timeout=timeout
    def fetch(self,feed_url:str,source:str,fetcher=None)->list[RSSArticle]:
        if not feed_url: raise ValueError("feed_url is required")
        if fetcher is None:
            def fetcher(u):
                with urlopen(Request(u,headers={"User-Agent":"Tradeapp/1.0"}),timeout=self.timeout) as r: return r.read()
        root=ET.fromstring(fetcher(feed_url)); out=[]
        for item in root.iter():
            if item.tag.rsplit("}",1)[-1]!="item": continue
            values={c.tag.rsplit("}",1)[-1]:(c.text or "").strip() for c in item}
            if not values.get("title"): continue
            try: published=parsedate_to_datetime(values.get("pubDate","")).astimezone(timezone.utc)
            except (TypeError,ValueError): published=datetime.now(timezone.utc)
            out.append(RSSArticle(values["title"],source,published,values.get("link","")))
        return out
