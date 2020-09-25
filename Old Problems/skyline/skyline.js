var getSkyline = function(buildings) {
    var res = [], height = [], pq = [0], prevMax = null;
    for(var b of buildings) {
        height.push([b[0], -b[2]]);
        height.push([b[1],  b[2]]);
    }
    height.sort((a, b) => {
        if(a[0] === b[0])  return a[1] - b[1];
        return a[0] - b[0];
    });

    for(var h of height) {
        if(h[1] < 0) {
            pq.push(-h[1]);
        } else {
            remove(pq, h[1]);
        }

        var maxV = Math.max(...pq);
        if(prevMax !== maxV) {  // maxV changed after remove h[1]
            res.push([h[0], maxV]);
            prevMax = maxV;
        }
    }
    return res;
};

var remove = function(arr, val) { // remove the first element equal to val
    var ind = -1;
    for(var i=0; i<arr.length; i++) {
        if(val === arr[i]) {
            ind = i;
            break;
        }
    }
    arr.splice(ind, 1);
    return;
};
