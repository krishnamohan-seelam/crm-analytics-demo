import streamlit as st

def create_booth_index(data):
    indexed_data = {}
    for booth in data.get('polling_booths'): 
        key = booth.get('polling_booth')
        indexed_data[key] = booth.get("polling_agent")
    return indexed_data

class SideBarController():
    
    def __init__(self,model,view) -> None:
        self.model = model
        self.view = view
        self.agent = None
        self.polling_booth = None

    def show_sidebar(self):
        with self.view.sidebar:
            self.view.render_title("Constituency Name", self.model.constituency_name )
            self.polling_booth = self.view.render_polling_booth(self.model.polling_booths)
            agents = self.model.get_agents(self.polling_booth)
            self.agent = self.view.render_agents(agents)
            

class SideBarModel():
    def __init__(self,data):
        self.data = data
        self.booth_agents_idx= create_booth_index(self.data)  
        self.constituency_name = self.data.get('constituency_name','DEFAULT')
        self.polling_booths= list(self.booth_agents_idx.keys())

    
    @property
    def constituency_name(self):
        return self._constituency_name

    @constituency_name.setter
    def constituency_name(self,val):
        self._constituency_name =val;

    @property
    def polling_booths(self):
        return self._polling_booths

    @polling_booths.setter
    def polling_booths(self, val):
        self._polling_booths = val
    
    def get_agents(self, polling_booth):
        agents =[ v for k,v in self.booth_agents_idx[polling_booth].items()]
        return agents

class SideBarView(object):

    def __init__(self):
        self.sidebar = st.sidebar

    def render_title(self,label,title):
        st.write(label) 
        st.title(title)

    def render_polling_booth(self, polling_booths):
        return st.selectbox(label = "Polling Booth Id",options = polling_booths)    

    def render_agents(self,agents):
         return st.selectbox(label = "Agent", options =agents)      



