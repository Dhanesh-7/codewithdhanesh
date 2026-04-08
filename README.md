# Public Problem Reporting System

A full-stack web application for municipal complaint management.

---

## Quick Start

### 1. Setup server

```bash
cd server
npm install
cp .env.example .env
# Fill in your values in server/.env
node seed.js        # Creates admin account + sample data
npm run dev         # Starts on http://localhost:5000
```

### 2. Setup client

```bash
cd client
npm install
cp .env.example .env
# Fill in your values in client/.env
npm run dev         # Starts on http://localhost:5173
```

---

## Environment Variables

### server/.env
```
PORT=5000
MONGODB_URI=mongodb+srv://<user>:<pass>@cluster.mongodb.net/municipal
JWT_SECRET=your_long_random_secret
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your@gmail.com
SMTP_PASS=your_gmail_app_password
CLIENT_URL=http://localhost:5173
```

### client/.env
```
VITE_API_URL=http://localhost:5000
VITE_GOOGLE_MAPS_KEY=your_google_maps_key
```

---

## Admin Login (after seeding)

- URL: http://localhost:5173/admin/login
- Email: admin@municipal.gov
- Password: Admin@123

---

## Pages

| URL | Description |
|-----|-------------|
| / | Home page |
| /report | Submit complaint (4-step form) |
| /track/:no | Track complaint by number |
| /admin/login | Admin login |
| /admin/dashboard | Stats + charts |
| /admin/complaints | All complaints with filters |
| /admin/complaints/:id | Complaint detail + actions |
| /admin/map | Full-screen map view |

---

## Tech Stack

- **Frontend**: React 18 + Tailwind CSS + Vite
- **Backend**: Node.js + Express.js
- **Database**: MongoDB Atlas + Mongoose
- **Storage**: Cloudinary
- **Maps**: Google Maps API
- **Auth**: JWT
- **Email**: Nodemailer (Gmail)
