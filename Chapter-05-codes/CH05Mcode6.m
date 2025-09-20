%This code fits a nonlinear least
%square curve to fit data points 
%using 'lsqcurvefit' function
clc; clear; close all;
set(0,'defaultaxesfontsize',29);
% Input data,head (H),discharge (Q)
H=[0.5,1.0,1.5,2.0,2.5,3.0];%in meter
Q=[15,50,100,180,280,400];%in m^3/s
%Define function: Q = C * H^n
modelF= @(par,H) par(1)*H.^par(2); 
ini_Guess=[1,1];% Initial guess for C&n
%Fit nonlinear model using lsqcurvefit
par=lsqcurvefit(modelF,ini_Guess,H,Q);
% Display the results
fprintf(['Parameters: C=%.4f, ' ...
    'n=%.4f \n'],par(1),par(2));
%predictions using fitted model
H_pred=linspace(min(H),max(H),100);
Q_pred=modelF(par, H_pred);%Calculate Q
% Plot original data and fitted curve
figure; subplot('position',[.2 .2 .6 .7]);
plot(H,Q,'ro','MarkerSize',12,'linewidth',2);
hold on; set(gca,'linewidth',2);
plot(H_pred,Q_pred,'b-','LineWidth',2);%Fitted
grid on; xlim([0 3.2]);ylim([0 410]);
xlabel('Head, H (m)');
ylabel('Discharge, Q (m^3/s)');
legend('Measured Data','Fitted Curve',...
    'Location','southeast');
% End of M - file
