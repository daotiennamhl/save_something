var tip = 100;
(
    function() {
        console.log("I have a " + husband());
        console.log(tip);
        function wife() {
            return tip*2;
        }
        function husband() {
            return wife()/2;
        }

        var tip = 10;
    }
)();