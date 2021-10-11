from flask import Flask, current_app, request, jsonify, Response
import dataframeconvertor
import currentstockcrawler
import json
app = Flask (__name__)
 



@app.route('/predict/MACD', methods=['GET'])
def makeMACD():
    # prices=db.throwQuery("""SELECT name, COUNT(*) from price GROUP BY name;""")ß
    # return str(prices)
    stock_name = request.args.get('name')
    targetDf = dataframeconvertor.getEMA_MACD(stock_name)
    # print(targetDf)
    resultDf = targetDf.to_json(orient="index", force_ascii=False, date_format='iso')
    # print(resultDf)
    return Response(resultDf, content_type='application/json; charset=utf-8')
    

@app.route('/predict/recommendStock', methods=['GET'])
def makeRecommand():
    # prices=db.throwQuery("""SELECT name, COUNT(*) from price GROUP BY name;""")
    # return str(prices)
    stock_name = request.args.get('name')
    targetDf = dataframeconvertor.getEMA_MACD(stock_name)
    # print(targetDf)
    resultDf = targetDf.iloc[-1].to_json(orient="index", force_ascii=False, date_format='iso')
    # print(resultDf)
    return Response(resultDf, content_type='application/json; charset=utf-8')



@app.route('/curprice', methods=['GET'])
def stockPrice():
    
    stockCode = request.args.get('code')
    time, price = currentstockcrawler.crawlStockData(stockCode)
    
    bodyData = {}
    bodyData['time'] = time
    bodyData['price'] = price
    bodyJson = json.dumps(bodyData)
    
    return Response(bodyJson, content_type='application/json; charset=utf-8')
        
if __name__ == "__main__":
    app.run()

