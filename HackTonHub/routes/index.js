"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/*
 * GET home page.
 */
const express = require("express");
const router = express.Router();
const request = require('request');
router.get('/', (req, res) => {
    var myJson = undefined;
    var todayDate = new Date();
    var day = todayDate.getDate().toString();
    var month = (todayDate.getMonth() + 1).toString();
    var year = todayDate.getFullYear().toString();
    if (parseInt(month) < 10)
        month = '0' + month;
    if (parseInt(day) < 10)
        day = '0' + day;
    var requestDate = year + '-' + month + '-' + day;
    request('https://intra.epitech.eu/auth-9c425ec84ab5ae69b14575278bb4d0e125f3d5c0/planning/load?format=json&start=' + requestDate + '&end=' + requestDate, { json: true }, (err, response, body) => {
        if (err) {
            return console.log(err);
        }
        try {
            myJson = JSON.parse(JSON.stringify(response.body));
            res.render('index', { json: myJson });
        }
        catch (e) {
            console.error("Parsing error:", e);
        }
    });
});
exports.default = router;
//# sourceMappingURL=index.js.map