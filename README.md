## README

### Coding Challenge Assumptions:

Project written under the assumption of controlling our valve with a RasPi. This script also assumes an intermediate stepper motor control board that supplies power and controls the required coils and receives step and direction inputs from the RasPi.

Sensor provided by https://www.ifm.com/de/en/product/IN5327?tab=details
has an output function of 2x normally open. Assuming there are two circuits, one detecting a "closed" state and the other an "open" state, where a closed circuit determines a position.

Valve is a double-acting actuator, so we need to drive the motor in two directions:
 https://us.misumi-ec.com/vona2/detail/221000099654/?HissuCode=C-UTE-50A&gclid=CjwKCAjwuYWSBhByEiwAKd_n_qlhjHMMPqnV8edrhrl9CkPO6bRHT5zkvve7IKfm-bHgQNKih050PhoCGrcQAvD_BwE&curSearch=%7b%22field%22%3a%22%40search%22%2c%22seriesCode%22%3a%22221000099654%22%2c%22innerCode%22%3a%22%22%2c%22sort%22%3a1%2c%22specSortFlag%22%3a0%2c%22allSpecFlag%22%3a0%2c%22page%22%3a1%2c%22pageSize%22%3a%2260%22%2c%2200000030969%22%3a%22k%22%2c%22jp000032588%22%3a%22mig00000000053035%22%2c%22jp000032596%22%3a%22mig00000000053031%22%2c%22jp000032600%22%3a%22mig00000000053032%22%7d&Tab=codeList

Open direction is assumed to be counterclockwise and logic HIGH, close as clockwise and logic LOW.
