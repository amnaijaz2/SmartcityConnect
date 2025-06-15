
  document.addEventListener('DOMContentLoaded', function() {
    // Handle service selection
    document.querySelectorAll('#dropdownMenuButton1 + .dropdown-menu .dropdown-item').forEach(item => {
      item.addEventListener('click', function(e) {
        e.preventDefault();
        const value = this.getAttribute('data-value');
        document.getElementById('selectedService').value = value;
        document.getElementById('dropdownMenuButton1').textContent = value;
      });
    });
  
    // Handle city selection
    document.querySelectorAll('#dropdownMenuButton2 + .dropdown-menu .dropdown-item').forEach(item => {
      item.addEventListener('click', function(e) {
        e.preventDefault();
        const value = this.getAttribute('data-value');
        document.getElementById('selectedCity').value = value;
        document.getElementById('dropdownMenuButton2').textContent = value;
      });
    });
  
    // Form submission
    document.getElementById('searchForm').addEventListener('submit', function(e) {
      e.preventDefault();
      
      const location = document.getElementById('inputSearch').value;
      const service = document.getElementById('selectedService').value;
      const city = document.getElementById('selectedCity').value;
      
      if (!location || !service || !city) {
        alert('Please fill all fields: location, service, and city');
        return;
      }
      
      // Here you would typically redirect or perform search
      // For example:
      window.location.href = `/search?location=${encodeURIComponent(location)}&service=${encodeURIComponent(service)}&city=${encodeURIComponent(city)}`;
    });
  });
  


  document.addEventListener('DOMContentLoaded', function() {
      // Copy phone number functionality
      document.querySelectorAll('.copy-btn').forEach(button => {
          button.addEventListener('click', function() {
              const phoneNumber = this.getAttribute('data-phone');
              
              // Create a temporary input element
              const tempInput = document.createElement('input');
              tempInput.value = phoneNumber;
              document.body.appendChild(tempInput);
              
              // Select and copy the text
              tempInput.select();
              document.execCommand('copy');
              
              // Remove the temporary input
              document.body.removeChild(tempInput);
              
              // Change button text temporarily to show success
              const originalText = this.innerHTML;
              this.innerHTML = '<i class="fas fa-check me-1"></i> Copied!';
              
              // Revert after 2 seconds
              setTimeout(() => {
                  this.innerHTML = originalText;
              }, 2000);
          });
      });
      
      // For desktop devices, modify the call button behavior
      document.querySelectorAll('.call-btn').forEach(button => {
          // Check if it's a mobile device
          const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
          
          if (!isMobile) {
              // For desktop, change the link to a click handler that shows the number
              button.addEventListener('click', function(e) {
                  e.preventDefault();
                  const phoneNumber = this.getAttribute('href').replace('tel:', '');
                  alert(`Please call: ${phoneNumber}\n\nOn mobile devices, this would automatically dial the number.`);
              });
          }
      });
  });
  