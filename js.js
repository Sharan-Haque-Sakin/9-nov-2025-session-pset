  // static credentials
  const validUser = "nayer25";
  const validPass = "jmc_2000";

  document.getElementById("loginBtn").addEventListener("click", function() {
      const user = document.getElementById("username").value;
      const pass = document.getElementById("password").value;

      if (user === validUser && pass === validPass) {
          downloadPset();
      } else {
          alert("Incorrect ID or password.");
      }
  });

  function downloadPset() {
      const link = document.createElement("a");
      link.href = "pset.pdf";       // your file in same directory
      link.download = "pset.pdf";   // name for download
      link.click();
  }