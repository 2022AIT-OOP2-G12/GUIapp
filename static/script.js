const rgbsub = document.querySelector('#RGBsubmit')
rgbsub.addEventListener('click', (e) => {
  console.log('rgbsubmit動いた')

  const Rin = document.getElementById('R_input').value
  const Gin = document.getElementById('G_input').value
  const Bin = document.getElementById('B_input').value

//   if (R_input.value != null) {
//     Rin = document.getElementById('R_input').value
//   }
//   if (G_input.value != null) {
//     Gin = document.getElementById('G_input').value
//   }
//   if (B_input.value != null) {
//     Bin = document.getElementById('B_input').value
//   }
  console.log(Rin,Gin,Bin)

  fetch('/address?', { method: 'POST', body: param }).then((response) => {
    console.log(response)

    view()
  })
})

const psub = document.querySelector('#photosubmit')

psub.addEventListener('click', (e) => {
  console.log('photosubmit動いた')
  const photo = document.getElementById('image').value

  let error_message = ''
  if (!photo && photo === '') error_message += '画像を入力してください'

  console.log(photo)

  fetch('/address?', { method: 'POST', body: param }).then((response) => {
    console.log(response)

    view()
  })
})
