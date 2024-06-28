from pymongo import MongoClient

# Conexión a DB local
#db_client = MongoClient().local


# Conexión a DB remota
db_client = MongoClient("mongodb+srv://pablohur:bAU1NOC1H7GrPLj7@cluster0.a8p20zh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").phd