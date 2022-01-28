import JarredFS

class AzureFS(JarredFS):
    def SaveFile(self):
        print("Azure")