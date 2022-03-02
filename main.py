from flask import Flask, render_template, request, jsonify
import sql

app = Flask(__name__) #name of current module

@app.route('/mySQL_postman',methods=['POST']) #for calling API from Postman and route tells which URL should call this function
def mySql_operations_via_postman():
    if(request.method=='POST'):
        operation=request.json['operation']
        host=request.json['host']
        user=request.json['user']
        password=request.json['password']
        db=request.json['db']
        mySql_obj=sql.MySql(host,user,password,db)
        mySql_obj.establishConnection()
        table_name=request.json['table_name']
        columns=request.json['columns']

        if operation=='create table':
            mySql_obj.createTable(table_name,columns)

    return jsonify("Table Created")



if __name__=='__main__':
    app.run() #To run application on local development server