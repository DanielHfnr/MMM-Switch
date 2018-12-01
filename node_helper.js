'use strict';

/* Magic Mirror
 * Module: MMM-Switch
 * 
 * By Daniel Hafner
 * MIT Licensed
 */

const NodeHelper = require('node_helper');

const PythonShell = require('python-shell');
var pythonStarted = false


module.exports = NodeHelper.create({


  python_start: function () {
    const self = this;
    const pyshell = new PythonShell('modules/' + this.name + '/distance_measuring/distance_measure.py', { mode: 'json', args: [JSON.stringify(this.config)]});

    pyshell.on('message', function (message) {
      
    
      if (message.hasOwnProperty('status')){
      console.log("[" + self.name + "] " + message.status);
      }
      if (message.hasOwnProperty('movement')){
        console.log("[" + self.name + "] " + "Detected movement: " + message.movement);
        self.sendSocketNotification('movement', message.movement);
        }
     
    });

    pyshell.end(function (err) {
      if (err) throw err;
      console.log("[" + self.name + "] " + 'finished running...');
    });
  },
  
  // Subclass socketNotificationReceived received.
  socketNotificationReceived: function(notification, payload) {
    if(notification === 'CONFIG') {
    	console.log("mmm-switch config loaded");
      this.config = payload
      if(!pythonStarted) {
        pythonStarted = true;
        this.python_start();
       };
    };
  }
  
});