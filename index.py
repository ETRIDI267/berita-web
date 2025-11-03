from flask import Flask, render_template_string

app = Flask(_name_)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Cafe Solaria - Luxury Taste</title>
      <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
      <style>
        * {margin:0; padding:0; box-sizing:border-box; scroll-behavior:smooth;}
        body {
          font-family: 'Poppins', sans-serif;
          background-color: #fff;
          color: #111;
          overflow-x: hidden;
        }

        header {
          background-color: #000;
          color: #fff;
          padding: 20px 50px;
          display: flex;
          justify-content: space-between;
          align-items: center;
          position: sticky;
          top: 0;
          z-index: 10;
          border-bottom: 2px solid #fff;
          animation: fadeDown 1s ease;
        }

        @keyframes fadeDown {
          from {opacity: 0; transform: translateY(-20px);}
          to {opacity: 1; transform: translateY(0);}
        }

        header h1 {color: #fff; letter-spacing: 2px;}

        nav a {
          color: #fff;
          text-decoration: none;
          margin: 0 15px;
          font-weight: 500;
          transition: color 0.3s;
        }
        nav a:hover {color: #d4af37;}

        .hero {
          height: 90vh;
          background: url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1600&q=80') center/cover no-repeat;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          text-align: center;
          color: white;
          position: relative;
          animation: fadeIn 1.5s ease;
        }

        .hero::after {
          content: "";
          position: absolute;
          inset: 0;
          background: rgba(0, 0, 0, 0.4);
        }

        .hero h2 {
          font-size: 50px;
          z-index: 2;
          animation: textSlideUp 1.5s ease;
        }

        .hero p {
          font-size: 18px;
          max-width: 600px;
          margin-top: 10px;
          z-index: 2;
          animation: fadeIn 2s ease;
        }

        @keyframes fadeIn {
          from {opacity: 0;}
          to {opacity: 1;}
        }

        @keyframes textSlideUp {
          from {opacity: 0; transform: translateY(30px);}
          to {opacity: 1; transform: translateY(0);}
        }

        .btn {
          background: #000;
          color: #fff;
          padding: 12px 30px;
          border-radius: 30px;
          text-decoration: none;
          font-weight: 600;
          margin-top: 20px;
          z-index: 2;
          border: 2px solid white;
          transition: all 0.3s;
        }

        .btn:hover {
          background: #fff;
          color: #000;
          box-shadow: 0 0 20px #d4af37;
        }

        section {padding: 80px 10%; transition: all 1s ease;}
        .fade-in {opacity: 0; transform: translateY(40px);}
        .show {opacity: 1; transform: translateY(0);}

        .menu {
          background: #f9f9f9;
        }

        .menu h2, .about h2, .contact h2 {
          text-align: center;
          font-size: 36px;
          margin-bottom: 50px;
        }

        .menu-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
          gap: 30px;
        }

        .menu-item {
          background: #fff;
          border-radius: 15px;
          box-shadow: 0 5px 20px rgba(0,0,0,0.1);
          overflow: hidden;
          transition: transform 0.3s, box-shadow 0.3s;
        }

        .menu-item:hover {
          transform: scale(1.05);
          box-shadow: 0 0 25px rgba(0,0,0,0.2);
        }

        .menu-item img {
          width: 100%;
          height: 200px;
          object-fit: cover;
        }

        .menu-item h3 {text-align: center; margin: 15px 0 5px;}
        .menu-item p {text-align: center; color: #555; margin-bottom: 15px;}

        .about {
          background-color: #fff;
          color: #111;
          text-align: center;
          line-height: 1.8;
        }

        .about p {
          max-width: 800px;
          margin: 0 auto;
          font-size: 17px;
          color: #333;
        }

        .contact {
          background-color: #f9f9f9;
          text-align: center;
        }

        .contact p {font-size: 17px; margin-bottom: 20px;}
        .contact a {
          color: #000;
          text-decoration: none;
          font-weight: 600;
          border: 2px solid #000;
          padding: 10px 20px;
          border-radius: 25px;
          transition: all 0.3s;
        }

        .contact a:hover {
          background-color: #000;
          color: #fff;
          box-shadow: 0 0 20px #d4af37;
        }

        footer {
          background: #000;
          color: #ccc;
          text-align: center;
          padding: 20px;
          border-top: 2px solid #fff;
          margin-top: 80px;
        }
      </style>
    </head>
    <body>

      <header>
        <h1>Cafe Solaria</h1>
        <nav>
          <a href="#home">Home</a>
          <a href="#menu">Menu</a>
          <a href="#about">About</a>
          <a href="#contact">Contact</a>
        </nav>
      </header>

      <section class="hero fade-in" id="home">
        <h2>Luxury Taste, Elegant Space</h2>
        <p>Nikmati sensasi rasa premium dalam suasana modern minimalis yang menenangkan.</p>
        <a href="#menu" class="btn">Lihat Menu</a>
      </section>

      <section class="menu fade-in" id="menu">
        <h2>Menu Favorit Kami</h2>
        <div class="menu-grid">
          <div class="menu-item">
            <img src="https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80" alt="Steak">
            <h3>Steak Premium</h3>
            <p>Rp85.000</p>
          </div>
          <div class="menu-item">
            <img src="https://images.unsplash.com/photo-1601924570668-3c31b6f3e2a1?auto=format&fit=crop&w=800&q=80" alt="Pasta">
            <h3>Italian Pasta</h3>
            <p>Rp55.000</p>
          </div>
          <div class="menu-item">
            <img src="https://images.unsplash.com/photo-1551218808-94e220e084d2?auto=format&fit=crop&w=800&q=80" alt="Dessert">
            <h3>Chocolate Dessert</h3>
            <p>Rp45.000</p>
          </div>
        </div>
      </section>

      <section class="about fade-in" id="about">
        <h2>Tentang Kami</h2>
        <p>Cafe Solaria berdiri dengan visi menghadirkan cita rasa terbaik dan pengalaman bersantap yang tak terlupakan.
           Kami percaya bahwa setiap hidangan bukan hanya tentang rasa, tetapi juga suasana yang mendukung kehangatan.
           Dengan desain modern minimalis dan pelayanan ramah, Cafe Solaria menjadi tempat sempurna untuk menikmati
           waktu bersama keluarga, teman, maupun pasangan.</p>
      </section>

      <section class="contact fade-in" id="contact">
        <h2>Hubungi Kami</h2>
        <p>📍 Alamat: Jl. Raya Bogor No. 45, Kota Bogor</p>
        <p>📞 Telepon: 0812-3456-7890</p>
        <p>📧 Email: info@cafesolaria.com</p>
        <a href="https://wa.me/6281234567890" target="_blank">Chat via WhatsApp</a>
      </section>

      <footer>
        © 2025 Cafe Solaria. All Rights Reserved.
      </footer>

      <script>
        const sections = document.querySelectorAll('.fade-in');
        const observer = new IntersectionObserver(entries => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              entry.target.classList.add('show');
            }
          });
        }, { threshold: 0.2 });
        sections.forEach(section => observer.observe(section));
      </script>

    </body>
    </html>
    """
    return render_template_string(html)

if _name_ == '_main_':
    app.run(debug=True)