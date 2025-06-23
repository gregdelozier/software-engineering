const assert = require('assert');

function parse(s) {
    let sign = 1;
    let fraction = 1.0;
    let decimal = false;
    if (s[0] === '-') {
        sign = -1;
        s = s.slice(1);
    }
    let n = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c === '.') {
            assert(decimal === false);
            decimal = true;
            continue;
        }
        if (decimal) {
            fraction = fraction * 0.1;
            n = n + (c.charCodeAt(0) - '0'.charCodeAt(0)) * fraction;
        } else {
            n = n * 10 + (c.charCodeAt(0) - '0'.charCodeAt(0));
        }
    }
    return n * sign;
}

function testSingleDigits() {
    assert.notStrictEqual(parse("1"), null);
    assert.strictEqual(parse("1"), 1);
    assert.strictEqual(parse("2"), 2);
    "0123456789".split('').forEach(s => {
        assert.strictEqual(String.fromCharCode(parse(s) + '0'.charCodeAt(0)), s);
    });
}

function testMultipleDigits() {
    assert.strictEqual(parse("123"), 123);
    assert.strictEqual(parse("123456"), 123456);
}

function testNegativeNumbers() {
    assert.strictEqual(parse("-123"), -123);
    assert.strictEqual(parse("-123456"), -123456);
}

function testDecimalNumbers() {
    assert.strictEqual(parse("1.23"), 1.23);
    assert.strictEqual(parse("123."), 123.0);
    assert(parse(".123") > 0.122999999 && parse(".123") < 0.123000001, `return = ${parse(".123")}`);
    assert.strictEqual(parse("-12.123"), -12.123);
}

function runAllTests() {
    testSingleDigits();
    testMultipleDigits();
    testNegativeNumbers();
    testDecimalNumbers();
    console.log("All tests passed.");
}

runAllTests();
