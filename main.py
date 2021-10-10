from flask import Flask, current_app, request, jsonify, Response
import dataframeconvertor
app = Flask (__name__)
 



@app.route('/predict/MACD', methods=['GET'])
def make_MACD():
    # prices=db.throwQuery("""SELECT name, COUNT(*) from price GROUP BY name;""")ß
    # return str(prices)
    stock_name = request.args.get('name')
    targetDf = dataframeconvertor.getEMA_MACD(stock_name)
    # print(targetDf)
    resultDf = targetDf.to_json(orient="index", force_ascii=False, date_format='iso')
    # print(resultDf)
    return Response(resultDf, content_type='application/json; charset=utf-8')
    

@app.route('/predict/recommendStock', methods=['GET'])
def make_Recommand():
    # prices=db.throwQuery("""SELECT name, COUNT(*) from price GROUP BY name;""")
    # return str(prices)
    stock_name = request.args.get('name')
    targetDf = dataframeconvertor.getEMA_MACD(stock_name)
    # print(targetDf)
    resultDf = targetDf.iloc[-1].to_json(orient="index", force_ascii=False, date_format='iso')
    # print(resultDf)
    return Response(resultDf, content_type='application/json; charset=utf-8')
        
if __name__ == "__main__":
    app.run()

