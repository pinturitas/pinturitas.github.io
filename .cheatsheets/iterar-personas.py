import yaml
f = open('personas.yml')
yaml_file = yaml.safe_load(f)
f0 = "id"
f1 = "alias"
f2 = "nombre"
f3 = "bio"

for data in yaml_file:
    f = open("temp/"+data[f0]+".md", "w")
#    texto = "---\n" + str(f0) + ": " + str(data[f0]) + "\n" + str(f1) + ": " + str(data[f1]) + "\n" + str(f2) + ": " + str(data[f2]) + "\n" + str(f3) + ": " + str(data[f3]) + "\n" + "---\n"
    texto = "---\nlayout: artista\nartista_id: " + str(data[f0]) + "\n" + "---\n"
    f.write(texto)
    f.close()

