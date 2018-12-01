/* Magic Mirror
 * Module: MMM-Switch
 * 
 * By Daniel Hafner
 * MIT Licensed
 */


Module.register("MMM-Switch", {
    defaults: {
        // trigger pin triggers both ultrasonic sensors
        triggerRightPin: 18,
        triggerLeftPin: 17,
        // both echo pins, use side the sensor is when you look at the mirror
        echoLeftPin: 23,
        echoRightPin: 24,
        // the max distances when a movement should count
        leftDistance: 10,
        rightDistance: 10,
        
        // update interval of the measurements
        intervall: 1,
    },
 
    start: function() {
        this.loaded = false;
        this.sendSocketNotification("CONFIG", this.config);
        Log.info('Starting module: ' + this.name);
    },

    socketNotificationReceived: function(notification, payload) {
        const self = this;
	if (notification === 'movement') {
            if (payload === "swipe_right") {
                this.sendNotification("PAGE_INCREMENT");
            } else if (payload === "swipe_left") {
                this.sendNotification("PAGE_DECREMENT");
            }
            this.updateDom();
            setTimeout(function () {
                self.updateDom(200);
            }, 2000);
        } 
    },
 	
}); 	
