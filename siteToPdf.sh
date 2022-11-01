#!/bin/bash
echo "Enter sitemap url: "
read sitemapUrl
npx website2pdf --sitemapUrl $sitemapUrl;
cd ./w2pdf_output;
cp ./../space_to_underscore.sh ./space_to_underscore.sh;
chmod 777 ./space_to_underscore.sh;
./space_to_underscore.sh;
pdfunite `find . -type f | grep .pdf` output.pdf;
mv ./output.pdf ./../;
cd ..;
rm -rf ./w2pdf_output
