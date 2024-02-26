// first code for carousel 
// Document ready function to ensure the DOM is fully loaded
$(document).ready(function() {
    // Initialize the carousel
    $('.carousel').carousel({
      interval: 3000, // Set the interval in milliseconds (e.g., 5000 for 5 seconds)
      pause: 'hover', // Pause on hover
      wrap: true // Enable continuous looping
    });
  });


// javascript for the product items in the carousel
$('#slider1, #slider2, #slider3').owlCarousel({
  loop: true,
  margin: 20,
  responsiveClass: true,
  responsive: {
      0: {
          items: 1,
          nav: false,
          autoplay: true,
      },
      600: {
          items: 3,
          nav: true,
          autoplay: true,
      },
      1000: {
          items: 5,
          nav: true,
          loop: true,
          autoplay: true,
      }
  }
})

// Ajax codes here for plus and minus + & - 

$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var elm=this.parentNode.children[2]
    $.ajax({
      type: "GET",
      url : "/pluscart",
      data:{
        prod_id:id
      },
      success:function(data){
        elm.innerText=data.quantity
        document.getElementById('amount').innerText = data.amount;
        document.getElementById('totalamount').innerText = data.totalamount;
        console.log(data)

      }
    })
})

//similary On  Minus-Cart copy 

$('.minus-cart').click(function () {
  var id = $(this).attr("pid").toString();
  var elm=this.parentNode.children[2]
  
  $.ajax({
    type: "GET",
    url : "/minuscart",
    data:{
      prod_id:id
    },
    success:function(data){
      elm.innerText=data.quantity
      document.getElementById('amount').innerText = data.amount;
      document.getElementById('totalamount').innerText = data.totalamount;
      console.log(data)

    }
  })
})
// remove cart
$('.remove-cart').click(function () {
  var id = $(this).attr("pid").toString();
  var elm=this
  
  $.ajax({
    type: "GET",
    url : "/removecart",
    data:{
      prod_id:id
    },
    success:function(data){
    
      document.getElementById('amount').innerText = data.amount;
      document.getElementById('totalamount').innerText = data.totalamount;
      console.log(data)
      elm.parentNode.parentNode.parentNode.parentNode.remove()

    }
  })
})