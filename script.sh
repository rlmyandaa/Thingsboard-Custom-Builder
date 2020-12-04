#copy and extract thingsboard.jar and thingsboard.yml
init() {
    cd put_your_modified_dependencies_here
    rm -rf .keep
    cd ..
}


getFile() {
    mkdir "copied_file"
    cp /etc/thingsboard/conf/thingsboard.yml copied_file
    cp /usr/share/thingsboard/bin/thingsboard.jar copied_file
}

extractFile() {
    mkdir -p "thingsboard_extract"
    (cd "thingsboard_extract" && exec jar -xf "../copied_file/thingsboard.jar")

    cd copied_file
    mv thingsboard.jar thingsboard_backup.jar
}

putFile() {
    #copy jar
    cp -r put_your_modified_dependencies_here/. thingsboard_extract/BOOT-INF/lib

    #copy yml
    cp copied_file/thingsboard.yml thingsboard_extract/BOOT-INF/classes
}

pack() {
    #pack
    mkdir -p "generated_file"
    cd thingsboard_extract
    jar cf0M ../generated_file/thingsboard.jar .
    cd ..

    #delete
    rm -r thingsboard_extract
}

case $1 in
    init) "$@"; exit;;
    getFile) "$@"; exit;;
    extractFile) "$@"; exit;;
    putFile) "$@"; exit;;
    pack) "$@"; exit;;
esac

