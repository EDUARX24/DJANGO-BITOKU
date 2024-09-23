// sweetalertUtil.js
function showNotification(data) {
  const { icon, title, text, redirect } = data;

  Swal.fire({
      title: title,
      text: text,
      icon: icon,
      showConfirmButton: true,
      confirmButtonText: "Aceptar",
      timer: 1500,
      timerProgressBar: true
  }).then(() => {
      if (redirect) {
          window.location.href = `/${redirect}`;
          cleanHistory();
      }
  });

  const cleanHistory = () => {
      if (redirect) {
          history.replaceState(null, null, `/${redirect}`);
      }
  };
}
