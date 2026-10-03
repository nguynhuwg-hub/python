from cloud_resource import Resource
class resource_manager:
    def __init__(self):
        self.resources = []

    def add_resource(self , resource):
        self.resources.append(resource)

    def list_resources(self):
        for resource in self.resources:
            print("--------------------")
            print("ID:", resource.resource_id)
            print("Name:", resource.name)
            print("CPU:", resource.cpu)
            print("RAM:", resource.ram)
            print("Status:", resource.status)

    def find_resource(self, resource_id):
        for resource in self.resources:
            if resource.resource_id == resource_id:
                return resource
          
        
        return None 
    
    def delete_resource(self, resource_id):
        resource = self.find_resource(resource_id)
        if resource is not None:
            self.resources.remove(resource)
            print("đã xoá resource")
        else:
            print("không tìm thấy resource")

    def start_resource(self, resource_id):

        resource = self.find_resource(resource_id)

        if resource is not None:
            resource.start()
            print("Resource da duoc start")
        else:
             print("Khong tim thay resource")


def show_menu():
    print("\n===== MINI CLOUD RESOURCE MANAGER =====")
    print("1. Add resource")
    print("2. List resources")
    print("3. Find resource")
    print("4. Delete resource")
    print("5. Start resource")
    print("6. Stop resource")
    print("0. Exit")

manager = resource_manager()


while True:
    show_menu()

    choice = input("Choose: ")

    if choice == "0":
        print("Goodbye!")
        break
    elif choice == "1":
        resource_id = input("Enter resource ID: ")
        name = input("Enter resource name: ")
        cpu = int(input("Enter CPU: "))
        ram = int(input("Enter RAM: "))

        resource = Resource(resource_id, name, cpu, ram)

        manager.add_resource(resource)

        print("Resource added successfully") 

    elif choice == "2":
        manager.list_resources()

    elif choice == "3":
        resource_id = input("Enter resource ID: ")

        resource = manager.find_resource(resource_id)

        if resource is not None:
            print("ID:", resource.resource_id)
            print("Name:", resource.name)
            print("CPU:", resource.cpu)
            print("RAM:", resource.ram)
            print("Status:", resource.status)
        else:
            print("Resource not found")
            
    elif choice == "4":
        resource_id = input("Enter resource ID: ")
        manager.delete_resource(resource_id)

    