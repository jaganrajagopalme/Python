exports.handler = async (event) => {
    // TODO implement
   var AWS= require('aws-sdk');
   var  ddb = new AWS.DynamoDB({apiVersion: '2012-08-10'});
   var param = {
       TableName:'Books',
       Items:{
           BookID:123,
           Name:'Thinking Creativity',
           Author:'James'
       }
   };
   
  // Call DynamoDB to add the item to the table
   ddb.putItem(params, function(err, data) {
    if (err) {
        console.log("Error", err);
    } 
    else {
      console.log("Success", data);
      }
    });

};