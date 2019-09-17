# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 17:07:43 2019

@author: tca
"""

from flask import Flask,jsonify
from py2neo import Graph
import json
from flask import request

 
app = Flask(__name__)
 

 
@app.route('/')
def index():
	return 'Hello,world!'
 
@app.route('/F_t_R/<string:id>',methods=['GET'])
def get_tasks(id):
    graph = Graph("http://localhost:7474",  username="neo4j",  password="123")
    res = graph.run("call allcomposition('1',4)")
    """ cypher = "match p = (n{name:'1'})-[r*0..4]-(x) return p LIMIT 10000 """
   
    cypher = "match p = (n{name:'"+ id + "'})-[r]-(x) return n,r,x LIMIT 10000"
    res = graph.run(cypher)
    ans = res.to_table()
    return jsonify(ans)
    
@app.route('/Fuck/<string:id>',methods=['GET'])
def get_task(id):
    graph = Graph("http://localhost:7474",  username="neo4j",  password="123")
    res = graph.run("call allcomposition('3',4)")
    """ cypher = "match p = (n{name:'1'})-[r*0..4]-(x) return p LIMIT 10000 """
    
    ans = res.data()
    s = str(ans)
    
    print(s)
    print("---------------------------------------------------------")
    json_data = json.dumps(s)
    return json_data
    
    
    
@app.route('/N_T_R/<string:id>/<string:n_t>',methods=['GET'])
def get_N_R(id,n_t):
    graph = Graph("http://localhost:7474",  username="neo4j",  password="123")
    res = graph.run("call allcomposition('1',4)")
    """ cypher = "match p = (n{name:'1'})-[r*0..4]-(x) return p LIMIT 10000 """
   
    cypher = "match p = (n{name:'"+id+"'})-[r*1.."+ n_t +"]-(x)"+ " return n,r,x LIMIT 10000"
    res = graph.run(cypher)
    ans = res.to_table()
    return jsonify(ans)



@app.route('/S_R',methods=['POST'])
def set_R():
    data = request.get_data()
    print(data)
    graph = Graph("http://localhost:7474",  username="neo4j",  password="123")
    res = graph.run("call allcomposition('1',4)")
    """ cypher = "match p = (n{name:'1'})-[r*0..4]-(x) return p LIMIT 10000 """
    json_data = json.loads(data)
    
    id1  = json_data.get("id1")
    id2  = json_data.get("id2")
    prop = json_data.get("prop")
   
    s = "{"
    for key in prop:
        s = s + key + ":"
        t = prop[key]
        
        t = '\'' + t + '\''
        s = s + t + ','
        prop[key] = t
    s = s[0:len(s) -1] + "}"
    print(s)
    print('------------------------------------------------------')
    
    
    cypher = "match p = (Id1{name:'"+id1+"'})-[r]-(Id2{name:'"+id2+"'}) SET r+="+s;
    print(cypher)
    res = graph.run(cypher)
    ans = res.to_table()
    return jsonify(ans)



@app.route('/S_N',methods=['POST'])
def set_N():
    data = request.get_data()
    print(data)
    graph = Graph("http://localhost:7474",  username="neo4j",  password="123")
    res = graph.run("call allcomposition('1',4)")
    """ cypher = "match p = (n{name:'1'})-[r*0..4]-(x) return p LIMIT 10000 """
    json_data = json.loads(data)
    
    id1  = json_data.get("id1")
    
    prop = json_data.get("prop")
   
    s = "{"
    for key in prop:
        s = s + key + ":"
        t = prop[key]
        
        t = '\'' + t + '\''
        s = s + t + ','
        prop[key] = t
    s = s[0:len(s) -1] + "}"
    print(s)
    print('------------------------------------------------------')
    
    
    cypher = "match p = (Id1{name:'"+id1+"'}) SET Id1+="+s;
    print(cypher)
    res = graph.run(cypher)
    ans = res.to_table()
    return jsonify(ans)




@app.route('/D_R/<string:id>',methods=['GET'])
def D_R(id):
    graph = Graph("http://localhost:7474",  username="neo4j",  password="123")
    res = graph.run("call allcomposition('1',4)")
    """ cypher = "match p = (n{name:'1'})-[r*0..4]-(x) return p LIMIT 10000 """
   
    cypher = "match p = (n)-[r{relation_id:'"+ id +"'}]-(x)" + " delete r"
    res = graph.run(cypher)
    ans = res.to_table()
    return jsonify(ans)
    
    

@app.route('/C_N/<string:id>',methods=['GET'])
def C_N(id):
    graph = Graph("http://localhost:7474",  username="neo4j",  password="123")
 
   
    cypher = "create (n:{name'"+ id +"'})"
    res = graph.run(cypher)
    ans = res.to_table()
    return jsonify(ans)





@app.route('/complex_Q',methods=['POST'])
def C_R():
    data = request.get_data()
    print(data)
    graph = Graph("http://localhost:7474",  username="neo4j",  password="123")
    res = graph.run(data)
    """ cypher = "match p = (n{name:'1'})-[r*0..4]-(x) return p LIMIT 10000 """
    ans = res.to_table()
    return jsonify(ans)
    
@app.route('/T_Q/<string:id>',methods=['GET'])
def T_Q(id):
    graph = Graph("http://localhost:7474",  username="neo4j",  password="123")
    
   
    cypher = "match p = (n)-[r]-(x)" +"where r.sTime >"+id +"AND r.eTime <"+id+ " return  p"
    res = graph.run(cypher)
    ans = res.to_table()
    return jsonify(ans)







@app.route('/D_N/<string:id>',methods=['GET'])
def D_N(id):
    graph = Graph("http://localhost:7474",  username="neo4j",  password="123")
    res = graph.run("call allcomposition('1',4)")
    """ cypher = "match p = (n{name:'1'})-[r*0..4]-(x) return p LIMIT 10000 """
   
    cypher ="match p = (n{name:'"+id+"'})-[r]-(x)"+ " delete n,r "
    res = graph.run(cypher)
    ans = res.to_table()
    return jsonify(ans)


    

if __name__ == '__main__':
    app.run(debug=True)
