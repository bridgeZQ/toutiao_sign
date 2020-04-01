const express = require('express');
const app = express();
var bodyParser = require('body-parser');
app.use(bodyParser());

var get_sgin = require('./get_signature');


app.post('/sign',
    function (req, res) {
        let result = req.body;
        let url = result.url;
        result = get_sgin.p(url);
        console.log(result);
        res.send(result)
    }
    );

app.listen(3000, () => {
    console.log('开启服务，端口3000')
    });


// res = get_sgin.p("/toutiao/c/user/article/?page_type=1&user_id=50502346173&max_behot_time=0&count=20");
// console.log(res);





