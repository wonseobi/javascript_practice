const day = 'thursday';

// Switch Case

switch(day) {
    case 'monday':
        console.log("Work my Miami Software Developer Job");
        console.log("Go to the Gym");
        break;
    case 'tuesday':
        console.log("Clean my room");
        break;
    case 'wednesday':
    case 'thursday':
        console.log("Get paid for my hard work");
    case 'friday':
        console.log("Record my own progress");
        break;
    case 'saturday':
    case 'sunday':
        console.log("Enjoy my weekend");
        break;
    default:
        console.log("Not a registered day");
}

// As an If Else...
if (day == 'monday') {
    console.log("It's a beautiful monday")
} else if (day == 'tuesday') {
    console.log("It's a beautiful tuesday")
} else if (day == 'wednesday' || day == 'thursday') {
    console.log("It's a beautiful middle of the week day")
} else if (day == 'friday') {
    console.log("It's a beautiful friday")
} else if (day == 'saturday' || day == 'sunday') {
    console.log("It's a beautiful weekend")
}