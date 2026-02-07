  document.getElementById("loginBtn").addEventListener("click", function() {
      const category = document.getElementById("categories").value;
      const fileName = category === "primary" ? "combi-pset-ghmo-raqin-tawhid.pdf" : "nt-pset-ghmo-ishtiaq-tawhid.pdf";

      downloadPset(fileName);
  });

  function downloadPset(fileName) {
      const link = document.createElement("a");
      link.href = fileName;       // file in same directory
      link.download = fileName;   // name for download
      link.click();
  }