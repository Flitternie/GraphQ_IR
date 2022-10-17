data=metaqa_data.tar.gz

if [ ! -e "$data" ] ; then
    echo "Start downloading metaqa-cypher dataset..."
    wget -c https://worksheets.codalab.org/rest/bundles/0x3ef513a9538246049720f63832289eb8/contents/blob/ -O $data
fi

tar -zxf $data
rm -rf $data