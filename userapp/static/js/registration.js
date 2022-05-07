//for date picker
$(function () {
  $("#datepicker").datepicker();
});

// border color
$('#firstname').keyup(function () {
  first = $('#firstname').val()
  if (first.length <= 4) {
    $('#firstname').css({
      borderColor: "red"
    })
  } else {
    $('#firstname').css({
      borderColor: "green"
    })

  }

});
$('#lastname').keyup(function () {
  last = $('#lastname').val()
  if (last.length <= 1) {
    $('#lastname').css({
      borderColor: "red"
    })
  } else {
    $('#lastname').css({
      borderColor: "green"
    })

  }

});
$('#email').keyup(function () {
  var mail = $('#email').val()
  if (mail.indexOf("@") < 0 || mail.indexOf(".") < 0) {
    $('#email').css({
      borderColor: "red"
    })
  } else {
    $('#email').css({
      borderColor: "green"
    })

  }

});
$('#mobile').keyup(function () {
  phone = $('#mobile').val()
  if (phone.length != 10) {
    $('#mobile').css({
      borderColor: "red"
    })
  }
  else if (isNaN(phone)) {
    $('#mobile').css({
      borderColor: "red"
    })

  } else {
    $('#mobile').css({
      borderColor: "green"
    })

  }


});
$('#age').keyup(function () {
  age = $('#age').val()
  if (age.length != 2) {
    $('#age').css({
      borderColor: "red"
    })
  }
  else if (isNaN(age)) {
    $('#age').css({
      borderColor: "red"
    })

  }

  else {
    $('#age').css({
      borderColor: "green"
    })

  }


});
// $('#address').keyup(function () {
//   adress = $('#address').val()
//   if (adress.length <= 10) {
//     $('#address').css({
//       borderColor: "red"
//     })
//   } else {
//     $('#address').css({
//       borderColor: "green"
//     })

//   }

// });
// $('#pin').keyup(function () {
//   pincode = $('#pin').val()
//   if (pincode.length != 6) {
//     $('#pin').css({
//       borderColor: "red"
//     })
//   }
//   else if (isNaN(pincode)) {
//     $('#pin').css({
//       borderColor: "red"
//     })

//   } else {
//     $('#pin').css({
//       borderColor: "green"
//     })

//   }
// });
// $('#place').keyup(function () {
//   place = $('#place').val()
//   if (place.length <= 5) {
//     $('#place').css({
//       borderColor: "red"
//     })
//   } else {
//     $('#place').css({
//       borderColor: "green"
//     })

//   }

// });


// end border color

categorieList = [
  { "categorie": "Electronics & Appliances", "SubCategories": ["Computer Repair", "Mobile Repair", "Tv Repair", "Cctv Repair", "Printer Repair", "Invertor Repair", "Water Pump Repair", "Chimney Repair", "Electric Geyser Repair", "Dishwasher Repair", "AC Repair", "DTH Repair", "Refrigerator Repair", "Washing Machine Repair"] },
  { "categorie": "Home Maintenance", "SubCategories": ["Carpentor", "Plumber", "Electrician", "Painting", "Interior Designor", "Architect", "Civil Contractor", "Rainwater Harvesting", "Gardeners", "Wielding Work", "Solar Heater Service", "False Celling", "Masonry Works", "Water Proofing", "Aluminum Fabrication"] },
  { "categorie": "Cleaning Service", "SubCategories": ["Pest Control", "Laundary", "Home Cleaing", "Water Tank Cleaing", "Bathroom Cleaing", "Drainage Cleaning", "Chimney Cleaning", "Glass Cleaning", "Aquarium Cleaning ", "Kitchen Cleaning", "Termite Cleaning"] },
  { "categorie": "Events & Occasions", "SubCategories": ["Wedding Planner", "Cake Delivery", "Birthday Planner", "Mehendi Planner", "Baby Shower", "Flower Decor", "Sangeet Planner", "Wedding Photography", "Pre-Wedding Photography", "Event Photography", "Baby Photography", "Portraits & Portfolio Shoot"] },
  { "categorie": "Health & Personals", "SubCategories": ["Physiotheraphy", "Yoga & Meditation", "Beauty Service", "Tailoring", "House Keeping", "Barbber", "Fitness Trainer", "Tattoo Artists", "Security Guards", "Astrology", "Bridal makeup", "Dietitian"] },
  { "categorie": "Automobile Services", "SubCategories": ["Car Wash", "Car Repair", "Bike Wash", "Bike Repair", "Driving school", "BreakDown Assistance"] },
  { "categorie": "Others", "SubCategories": ["Tution Teacher"] },
]





$(window).bind("load", function () {

  for (i in categorieList) {
    $('#selectbox').append("<Option value='" + categorieList[i].categorie + "'>" + categorieList[i].categorie + "</option>")
  }
});
$('#selectbox').click(function () {
  $('#SubCategories').empty()
  for (i in categorieList) {
    if (categorieList[i].categorie == $('#selectbox').val()) {
      // $('#SubCategories').HTML("")
      for (j in categorieList[i].SubCategories) {
        $('#SubCategories').show()
        $('#SubCategories').append("<Option value='" + categorieList[i].SubCategories[j] + "'>" + categorieList[i].SubCategories[j] + "</option>")

        // console.log(categorieList[i].SubCategories[j])
      }
    }
  }
})


// $('#selectbox').click(function () {
//   if ($('#selectbox').val() == "Others") {
//     $('#inputbox').show()

//   } else {
//     $('#inputbox').hide()
//   }
// });

// end check box




// validation

$('#form1').validate({
  rules: {
    firstname: {
      required: true,
      minlength: 6,
    },
    lastname: {
      required: true,
      minlength: 1,
    },
    username: {
      required: true,
      minlength: 6,
    },
    password: {
      required: true,
      minlength: 6,
    },
    c_password: {
      required: true,
      equalTo: "#password1",
    },
    email: {
      required: true,
      email: true,
    },
    phone: {
      required: true,
      number: true,
      minlength: 10,
      maxlength: 10,
    },
    dob: {
      required: true,
      date: true,
      dateFormat: true,
    },
    age: {
      required: true,
      number: true,
      minlength: 2,
    },
    address: {
      required: true,
    },
    addition: {
      required: true,
    },
    pin: {
      number:true,
      required: true,
      minlength: 6,
      maxlength: 6,
    },
    place: {
      required: true,
    },
    district: {
      required: true,
    },
    state: {
      required: true,
    },
    loca: {
      required: true,
    },
    educ: {
      required: true,
    },
  },
  messages: {
    firstname: {
      required: "Enter your First name",
      minlength: "alteast 6",
    },
    lastname: {
      required: "Enter your last name",
      minlength: "alteast 1",
    },
    username: {
      required: "Enter your Username",
      minlength: "alteast 6",
    },
    password: {
      required: "Enter your Password",
      minlength: "alteast 6",
    },
    c_password: {
      required: "conform your Password",
      equalTo: "password must be same"
    },
    email: {
      required: "Enter your Email Address",
      email: "Enter Valid Email Address",
    },
    phone: {
      required: "Enter your phone number",
      number: "Enter Number",
      minlength: "minimum length 10",
      maxlength: "Not more than 10"

    },
    dob: {
      required: "Enter Your Dob",
      date: "Select date",
      dateFormat: "(dd/mm/yyyy)",
    },
    age: {
      required: "Enter your age",
      number: "Enter Number",
      minlength: "You Should be above 2",
    },
    address: {
      required: "Enter your Address",
    },
    addition: {
      required: "Enter your additional Address",
    },
    pin: {
      required: "Enter your pincode number",
      number: "Enter Number",
      minlength: "minimum length 6",
      maxlength: "Not more than 6"

    },
    place: {
      required: "Enter your place",
    },
    district: {
      required: "Enter your district",
    },
    state: {
      required: "Enter your state",
    },
    loca: {
      required: "Enter your Location",
    },
    educ: {
      required: "Enter your Education Qualification",
    },
  },
  SubmitHandler: function (form1) {
    form.submit();
  }
})



  // end validation
