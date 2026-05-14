# Example: Using Methods and Attributes

# Example: Using Methods and Attributes

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Example: Using Methods and Attributes

Icon Progress Bar (browser only)

5 min read

### Rideshare Example

#### **![Rideshare driver using gps app on a highway.](https://moringa.instructure.com/courses/1406/files/625220/download) Business Problem**

Building on the rideshare business example from Classes and Instances, we want to create a standard blueprint that defines the business/process, allows storing info about the drivers, passengers, and trips, and integrate how different aspects of the business come together*—*making everything more efficient. It would be a huge time suck to have to re-code those essential attributes (driver, passenger, &c.) over and over again.

#### **Solution: Ride Class, Passenger Class, and Driver Class**

##### Ride Class

The Ride class represents a specific ride requested by a passenger and assigned to a driver. It has attributes such as ride\_id (a unique identifier), passenger (an instance of the Passenger class), driver (an instance of the Driver class), pickup\_location, dropoff\_location, start\_time, end\_time, and fare. These attributes store essential information about the ride, including the associated passenger and driver, the pickup and dropoff locations, the timestamps for the start and end of the ride, and the calculated fare.

The Ride class also has methods to facilitate the ride process. The assign\_driver() method is used to assign an available driver to the ride. The calculate\_fare() method calculates the fare based on factors such as distance and duration. The start\_ride() method marks the beginning of the ride and records the start time, while the end\_ride() method marks the completion of the ride, records the end time, and triggers the fare calculation.

* **Attributes:**  
  + **ride\_id:** a unique identifier for the ride
  + **passenger:** an instance of the Passenger class representing the passenger requesting the ride
  + **driver:** an instance of the Driver class representing the driver assigned to the ride
  + **pickup\_location:** the location where the passenger will be picked up
  + **dropoff\_location:** the location where the passenger will be dropped off
  + **start\_time:** the timestamp when the ride begins
  + **end\_time:** the timestamp when the ride ends
  + **fare:** the calculated fare for the ride
* **Methods:**  
  + **assign\_driver():** a method to assign an available driver to the ride
  + **calculate\_fare():** a method to calculate the fare based on factors such as distance and duration
  + **start\_ride():** a method to mark the start of the ride and record the start time
  + **end\_ride():** a method to mark the end of the ride, record the end time, and calculate the fare

##### Passenger Class

The Passenger class represents a user who uses the rideshare program to request rides. It has attributes such as passenger\_id (a unique identifier), name, contact\_info (e.g., phone number, email), and payment\_info (e.g., credit card details). These attributes store essential information about the passenger, allowing them to be identified, contacted, and charged for the rides they take.

The Passenger class has methods that enable the passenger to interact with the rideshare system. The request\_ride() method allows the passenger to request a ride by providing the pickup and dropoff locations. The cancel\_ride() method allows the passenger to cancel a previously requested ride if needed. After the completion of a ride, the passenger can use the rate\_driver() method to provide feedback and rate the driver's performance.

* **Attributes:**  
  + **passenger\_id:** a unique identifier for the passenger
  + **name:** the name of the passenger
  + **contact\_info:** the contact information of the passenger (e.g., phone number, email)
  + **payment\_info:** the payment information of the passenger (e.g., credit card details)
* **Methods:**  
  + **request\_ride():** a method to request a ride by providing the pickup and dropoff locations
  + **cancel\_ride():** a method to cancel a requested ride
  + **rate\_driver():** a method to rate the driver after the completion of a ride

##### Driver Class

The Driver class represents a driver who participates in the rideshare program and provides transportation services to passengers. It has attributes such as driver\_id (a unique identifier), name, vehicle\_info (e.g., make, model, license plate), availability\_status (indicating the driver's current availability), and rating (the average rating based on passenger feedback). These attributes store essential information about the driver, their vehicle, and their performance in the rideshare system.

The Driver class has methods that allow the driver to interact with the rideshare system and manage their rides. The accept\_ride() method is used by the driver to accept a ride request and update their availability status accordingly. The complete\_ride() method is used to mark the completion of a ride and update the driver's availability status. The update\_location() method allows the driver to update their current location, which can be used for ride matching and tracking purposes. The view\_ride\_history() method enables the driver to access their ride history and view their earnings.

* **Attributes:**  
  + **driver\_id:** a unique identifier for the driver
  + **name:** the name of the driver
  + **vehicle\_info:** information about the driver's vehicle (e.g., make, model, license plate)
  + **availability\_status:** the current availability status of the driver (e.g., available, busy)
  + **rating:** the average rating of the driver based on passenger feedback
* **Methods:**  
  + **accept\_ride():** a method to accept a ride request and update the driver's availability status
  + **complete\_ride():** a method to mark the completion of a ride and update the driver's availability status
  + **update\_location():** a method to update the driver's current location
  + **view\_ride\_history():** a method to view the driver's ride history and earnings

These classes and their attributes and methods provide a foundation for building a rideshare program. The Ride class acts as a central entity that connects the Passenger and Driver classes, facilitating the ride-matching process. The Passenger class represents the users who request rides, while the Driver class represents the service providers who fulfill those ride requests. The interaction between these classes, through their respective methods, enables the smooth operation of the rideshare system, from ride request to completion and payment.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243650

Scraped At: 2026-05-14T21:02:53.096166
