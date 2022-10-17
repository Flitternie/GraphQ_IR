data=overnight_data.tar.gz
evaluator=evaluator.tar.gz

if [ ! -e "$data" ] ; then
    echo "Start downloading overnight dataset..."
    wget -c https://worksheets.codalab.org/rest/bundles/0x34b628718e514100aa75731bbdef457f/contents/blob/ -O $data
fi

if [ ! -e "$evaluator" ]; then
    echo "Start downloading evaluator for overnight dataset ..."
    wget -c https://worksheets.codalab.org/rest/bundles/0x05625395eb1243ce9c2c75849a87f906/contents/blob/ -O $evaluator
# fi

tar -zxf $data
tar -zxf $evaluator
rm -rf $data
rm -rf $evaluator
cp data/overnight/evaluator/sempre/module-classes.txt .