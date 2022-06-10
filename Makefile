
build: out/project_template.zip

clean:
	rm -rf build out

rebuild: clean build

out/project_template.zip: export LC_ALL=C

out/project_template.zip:
	mkdir -p out
	mkdir -p build
	cp -R project_name build/project_name
	find build/ -type f | xargs sed -i.bak 's/project_name/\{project_name\}/g'
	zip -r $@ build/

