module.exports = {
  outputDir: '../static/js',
  publicPath: process.env.NODE_ENV === 'production' ? '/static/' : '/',
  devServer: {
    proxy: 'http://localhost:8000'
  }
}
