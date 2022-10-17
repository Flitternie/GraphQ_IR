ontology=grailqa_data_ontology.tar.gz

if [ ! -e "$ontology" ] ; then
    echo "Start downloading grailqa data ontology..."
    wget -c https://worksheets.codalab.org/rest/bundles/0xeee9c319d8884300b71498fdd54a6d7b/contents/blob/ -O $ontology
fi

tar -zxf $ontology
rm -rf $ontology