import React from 'react';

function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Navbar */}
      <header className="bg-blue-600 text-white p-4">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-lg font-bold">My Website</h1>
          <nav>
            <ul className="flex space-x-4">
              <li>
                <a href="#home" className="hover:underline">
                  Home
                </a>
              </li>
              <li>
                <a href="#about" className="hover:underline">
                  About
                </a>
              </li>
              <li>
                <a href="#contact" className="hover:underline">
                  Contact
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow container mx-auto p-4 text-center">
        <h2 className="text-2xl font-bold mb-4">Welcome to the Home Page</h2>
        <p className="text-gray-700">
          This is a simple React application styled with Tailwind CSS. Explore
          the website to learn more!
        </p>
      </main>

      {/* Footer */}
      <footer className="bg-blue-600 text-white p-4">
        <div className="container mx-auto text-center">
          <p>&copy; 2025 My Website. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default Home;
