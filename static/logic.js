//calling results from each ML model and putting them into the comparison table
function getRFData() {
  d3.json('/randomForest').then((data) => {
    let rfData = data;
    let tableBody = d3.select('#accuracy-table');
    var row = tableBody.append('tr');
    var model = row.append('td').text('Random Forest');
    var gen7_acc = row.append('td').text(rfData[0].Accuracy);
    var gen8_acc = row.append('td').text(rfData[1].Accuracy);
    var gen7_r2 = row.append('td').text(rfData[0].R2);
    var gen8_r2 = row.append('td').text(rfData[1].R2);
  });
}
getRFData();
function getNNData() {
  d3.json('/neuralNetwork').then((data) => {
    var nnData = data;
    let tableBody = d3.select('#accuracy-table');
    var row = tableBody.append('tr');
    var model = row.append('td').text('Neural Network');
    var gen7_acc = row.append('td').text(nnData[0].Accuracy);
    var gen8_acc = row.append('td').text(nnData[1].Accuracy);
    var gen7_r2 = row.append('td').text(nnData[0].R2);
    var gen8_r2 = row.append('td').text(nnData[1].R2);
  });
}
getNNData();
function getKNNData() {
  d3.json('/KNN').then((data) => {
    var knnData = data;
    let tableBody = d3.select('#accuracy-table');
    var row = tableBody.append('tr');
    var model = row.append('td').text('K Nearest Neighbor');
    var gen7_acc = row.append('td').text(knnData[0].Accuracy);
    var gen8_acc = row.append('td').text(knnData[1].Accuracy);
    var gen7_r2 = row.append('td').text(knnData[0].R2);
    var gen8_r2 = row.append('td').text(knnData[1].R2);
  });
}
getKNNData();
function getSVCData() {
  d3.json('/SVC').then((data) => {
    var svcData = data;
    let tableBody = d3.select('#accuracy-table');
    var row = tableBody.append('tr');
    var model = row.append('td').text('Support Vector Machine');
    var gen7_acc = row.append('td').text(svcData[0].Accuracy);
    var gen8_acc = row.append('td').text(svcData[1].Accuracy);
    var gen7_r2 = row.append('td').text(svcData[0].R2);
    var gen8_r2 = row.append('td').text(svcData[1].R2);
  });
}
getSVCData();
function getLRData() {
  d3.json('/logisticRegression').then((data) => {
    var lrData = data;
    let tableBody = d3.select('#accuracy-table');
    var row = tableBody.append('tr');
    var model = row.append('td').text('Logistic Regression');
    var gen7_acc = row.append('td').text(lrData[0].Accuracy);
    var gen8_acc = row.append('td').text(lrData[1].Accuracy);
    var gen7_r2 = row.append('td').text(lrData[0].R2);
    var gen8_r2 = row.append('td').text(lrData[1].R2);
  });
}
getLRData();

//calling results best model and putting them into the best model tables
function gen7LRTable() {
  d3.json('/logisticRegressionClassifications').then((data) => {
    d3.json('/logisticRegression').then((r2) => {
      var lrData = data;
      var r2Gen7 = r2[0].R2
      let tableBody = d3.select('#best-table-gen-7');
      var row = tableBody.append('tr');
      var rSquared = row.append('td').text(r2Gen7);
      var precision = row.append('td').text(lrData[0].weighted_avg);
      var recall = row.append('td').text(lrData[1].weighted_avg);
      var f1 = row.append('td').text(lrData[2].weighted_avg);
      var support = row.append('td').text(lrData[3].weighted_avg);
    });
  });
}
gen7LRTable();
function gen8LRTable() {
  d3.json('/logisticRegressionClassifications').then((data) => {
    d3.json('/logisticRegression').then((r2) => {
      var lrData = data;
      var r2Gen8 = r2[1].R2
      let tableBody = d3.select('#best-table-gen-8');
      var row = tableBody.append('tr');
      var rSquared = row.append('td').text(r2Gen8);
      var precision = row.append('td').text(lrData[4].weighted_avg);
      var recall = row.append('td').text(lrData[5].weighted_avg);
      var f1 = row.append('td').text(lrData[6].weighted_avg);
      var support = row.append('td').text(lrData[7].weighted_avg);
    });
  });
}
gen8LRTable();
