# ecg-kit-webapp
Webapp of ecg-kit matlab plugin with a fancy UX

##Build ecg-kit-webapp
```
npm run build
```

##Run ecg-kit-webapp
```
npm run start
```

##Setup Matlab
On Mac or Linux systems —
If you have the $MATHLABROOT variable declared pointing to your Mathlab instalation just run
```
npm run setup
```
Else
```
cd "<MATHLAB INSTALLATION PATH>/extern/engines/python" && python setup.py install
```
