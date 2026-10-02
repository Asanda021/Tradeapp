from dataclasses import dataclass
from urllib.parse import urlencode
from tradeapp.adapters.contracts import AccountConnection,AccountPermissions,ConnectionState

@dataclass(frozen=True)
class OAuthConfig:
    provider:str
    authorization_endpoint:str
    client_id:str
    redirect_uri:str
    scopes:tuple[str,...]=()
    def authorization_url(self,state:str)->str:
        if not state: raise ValueError("state is required")
        return self.authorization_endpoint+"?"+urlencode({"client_id":self.client_id,"redirect_uri":self.redirect_uri,"response_type":"code","scope":" ".join(self.scopes),"state":state})

class AccountConnectionService:
    def connected(self,provider:str,account_id:str,sandbox:bool=True,trading:bool=False,withdrawal:bool=False)->AccountConnection:
        if withdrawal: raise ValueError("withdrawal permission is forbidden")
        return AccountConnection(provider,account_id,sandbox,AccountPermissions(trading=trading,withdrawal=False),ConnectionState.CONNECTED)
