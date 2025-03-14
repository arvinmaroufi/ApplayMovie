let networkError = () => {
    Swal.fire({
        title: 'VPN وصل نیست',
        // icon: 'error',
        confirmButtonText: 'Ok',
        imageUrl: './img/svg/vpn.svg',
        imageWidth: 300,
        imageHeight: 150,
        imageAlt: 'Custom image',
    })
}
