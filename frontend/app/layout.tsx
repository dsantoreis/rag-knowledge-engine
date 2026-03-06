export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ fontFamily: 'Inter, sans-serif', background: '#0b1020', color: '#e8eeff', margin: 0 }}>
        {children}
      </body>
    </html>
  );
}
