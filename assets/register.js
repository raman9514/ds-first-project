function validation()
  { 
   
    var fullname=document.forms["reg_form"]["fullname"].value;
    var username=document.forms["reg_form"]["username"].value;
    var pass1=document.forms["reg_form"]["pass1"].value;
    var pass2=document.forms["reg_form"]["pass2"].value;
    var email1=document.forms["reg_form"]["email1"].value;
    var TnC =document.getElementById('TnC').checked;
    
  
    //-------------validate username----------// 
  
    if(null==username.match(/^[A-Za-z0-9]{2,30}$/))
    {
     document.forms["reg_form"]["username"].focus();
     document.forms["reg_form"]["username"].style.borderColor = "red";
     document.forms["reg_form"]["username"].style.color = "red";
     alert("UserName can only contain " + "\n" + "-> Upper Case (A-Z) " + "\n" + "-> lower case (a-z )and " + "\n" + "-> number (1-9)");
   return false; }
  
  
  
    // -----------Validate Full Name ---------// 
    if(null!=fullname.match(/^[A-Za-z]{2,30}\s/))
       { }
    else if(null!=fullname.match(/^[A-Za-z]{2,30}$/))
       {  }
    else{
      document.forms["reg_form"]["fullname"].focus();
      document.forms["reg_form"]["fullname"].style.borderColor = "red";
      document.forms["reg_form"]["fullname"].style.color = "red";
      alert("Please Enter Valid name");
      return false;
    } 
 

         
    // -------------validate email1----------//  
    if(email1=="")
    { 
     document.forms["reg_form"]["email1"].focus();
     document.forms["reg_form"]["email1"].style.borderColor = "red";
     document.forms["reg_form"]["email1"].style.color = "red";
   alert("Field Can't be empty");
    return false;   
    }

      
     //-------------validate Password----------//     
       if(pass1=="")
        {document.forms["reg_form"]["pass1"].focus();
         document.forms["reg_form"]["pass1"].style.borderColor = "red";
        
         alert("Please Enter Password");
         return false;}

       if(pass1!=pass2)
       { document.forms["reg_form"]["pass2"].focus();
         document.forms["reg_form"]["pass2"].style.borderColor = "red";
        
       alert("Password Not Matched");
     return false; }

     // ----------------- Term and Condition -------//

       if(TnC==false)
        {
          alert("Please Accept T&C");
        return false;}

    }


