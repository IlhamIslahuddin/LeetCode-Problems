/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
        var num = n - 1;
    return function() {
        num = num + 1;
        return num
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
