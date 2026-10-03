class Resource:
    def __init__(self,resource_id,name,cpu,ram):
        self.resource_id = resource_id
        self.name = name
        self.cpu = cpu
        self.ram = ram 
        self.status = "stopped"

    def start(self):
        self.status = "running"

    def stop(self):
        self.status = "stopped"