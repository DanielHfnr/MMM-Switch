# Module: MMM-Switch


`MMM-Switch` is a <a href="https://github.com/MichMich/MagicMirror">MagicMirror</a> addon module.
This module uses just one HC-SR04 ultrasonic sensors to determine hand position to produce a "Swipe Right".
The module is also prepared to use two ultrasonic sensor to also produce a "Swipe left".

## Installing the module
1. Navigate into your MagicMirror's `modules` folder and execute `git clone https://github.com/DanielHfnr/MMM-Switch.git`.  Change with cd into the new created folder named MMM-Switch.
2. Execute `npm install` to install the dependencies


To use this module, add it to the modules array in the `config/config.js` file:
````javascript
modules: [
	{
		module: 'MMM-Switch',
		position: 'middle_center',	// Doesn't matter after it's setup.  It should be blank.
									
		config: {
			// See 'Configuration options' for more information.
			module: 'MMM-Switch',
                        position: 'middle_center',
                        config: {
                        	triggerRightPin: 18,
                                triggerLeftPin: 17,
                                echoRightPin: 24,
                                echoLeftPin: 23,
                                leftDistance: 10,
                                rightDistance: 10,
                                intervall: 2,
				}	
		}
	}
]
````

## Configuration options

The following properties can be configured:


<table width="100%">
	<!-- why, markdown... -->
	<thead>
		<tr>
			<th>Option</th>
			<th width="100%">Description</th>
		</tr>
	<thead>
	<tbody>
		<tr>
			<td><code>echoLeftPin</code></td>
			<td>Left Sensor's Echo pin.<br>
				<br><b>Example:</b> <code>23</code>
				<br><b>Default Value:</b> <code>23</code>
			</td>
		</tr>
		<tr>
			<td><code>triggerLeftPin</code></td>
			<td>Left Sensor's Trigger pin.<br>
				<br><b>Example:</b> <code>17</code
				<br><b>Default Value:</b> <code>17</code>
			</td>
		</tr>
		<tr>
			<td><code>echoRightPin</code></td>
			<td>Right Sensor's Echo pin.<br>
				<br><b>Example:</b> <code>24</code>
				<br><b>Default Value:</b> <code>24</code>
			</td>
		</tr>
		<tr>
			<td><code>triggerRightPin</code></td>
			<td>GPIO pin that will be activated when you "press" the sensors.<br>
				<br><b>Example:</b> <code>18</code>
				<br><b>Default Value:</b> <code>18</code>
			</td>
		</tr>
		<tr>
			<td><code>leftDistance</code></td>
			<td>Distance in cm that will initiate the movement detection with the left sensor<br>
				<br><b>Example:</b> <code>10</code>
				<br><b>Default Value:</b> <code>10</code>
			</td>
		</tr>
		<tr>
			<td><code>rightDistance</code></td>
			<td>Distance in cm that will initiate the movement detection with the right sensor<br>
				<br><b>Example:</b> <code>10</code>
				<br><b>Default Value:</b> <code>10</code>
			</td>
		</tr>
		<tr>
                        <td><code>intervall</code></td>
                        <td>Time intervall when distance is measured by the sensor.<br>
                                <br><b>Example:</b> <code>2</code>
                                <br><b>Default Value:</b> <code>1</code>
                        </td>
                </tr>

	</tbody>
</table>
