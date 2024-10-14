import sys
import os

file_extension = ".vue"

folder_path = sys.argv[1]
component_name = sys.argv[2]
file_path = os.path.join(folder_path, component_name + file_extension)

path_exists_directory = os.path.exists(folder_path)
path_exists_file = os.path.exists(file_path)

def print_error_and_exit(text):
    print("Error: " + text)
    sys.exit()


if(not path_exists_directory):
    print_error_and_exit("Specified folder does not exist")

if(path_exists_file):
    print_error_and_exit("Specified component file already exists")

f = open(file_path, "w")
f.write("<template>\n")
f.write("</template>\n\n")
f.write("<script lang=\"ts\">\n")
f.write("import { Component, Vue } from 'vue-property-decorator';\n\n")
f.write("@Component({\n")
f.write("   components: {\n")
f.write("   },\n")
f.write("})\n")
f.write("export default class " + component_name + ' extends Vue {\n')
f.write("}\n")
f.write("</script>\n\n")
f.write("<style>\n")
f.write("</style>\n\n")