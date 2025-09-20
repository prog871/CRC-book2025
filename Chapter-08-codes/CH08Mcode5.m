%This code plots the PDF 
%and CDF for a dam problem
clc; clear; close all;
set(0,'defaultaxesfontsize',25)
% Step 1:Input the sample data 
data = [450,620,700,350,480,520,...
550,600,730,400,530,610,580,490,...
720,510,650,470,380,560,640,390,...
460,590,710,370,540,500,620,670, ...
510,680,420,570,630,...
460,690,580,410,530];
mu=mean(data); % Mean
sigma=std(data, 1);% std dev
% Step 3: Define flood threshold
flood1=700;% Flood threshold(m³/s)
% Step 4:flood risk probability
z_flood=(flood1-mu)/sigma;% z-score 
p_flood =1-normcdf(z_flood);% P(X>700)
flood_prcnt = p_flood * 100;
cdf_at_700=normcdf(z_flood);% CDF@700
% Step 5: Display result
fprintf('Mean (mu) = %.2f m³/s\n',mu);
fprintf('St Dev (sigma)=%.2f m³/s\n',sigma);
fprintf(['Flood Risk (P(X>700))' ...
    '= %.2f%%\n'], flood_prcnt);
% Subplot 1: plot PDF %%%%%%%%%%%%%%%
subplot('position',[0.09 .1 .37 .7]);
x = (mu - 4*sigma):0.1:(mu + 4*sigma);
pdf = normpdf(x, mu, sigma); %PDF
plot(x,pdf,'k-','LineWidth',2.5);
hold on; ylim([0 0.0041]);
x_flood=x(x >=flood1);% x values>700
pdf_flood=normpdf(x_flood,mu,sigma);%pdf
fill([x_flood fliplr(x_flood)],...
[pdf_flood zeros(size(pdf_flood))],'m', ...
'FaceAlpha', 0.3, 'DisplayName', ...
sprintf('P(X>700)=%.2f%%',flood_prcnt));
line([flood1 flood1],[0 100],...
'Color','b','LineStyle','--','LineWidth',2);
grid on;set(gca,'linewidth',1.5);
% Subplot 2: plot CDF %%%%%%%%%%%%%%% 
subplot('position',[.57 .1 .37 .7]); 
cdf = normcdf(x, mu, sigma); %CDF
plot(x,cdf,'k-','LineWidth',2.5);
hold on;ylim([0 1.05]);
line([flood1 flood1], [0 cdf_at_700],...
'Color','b','LineStyle','--','LineWidth',2);
line([0 flood1],...
[cdf_at_700 cdf_at_700],'Color','b',...
'LineStyle', '--','LineWidth', 2);
grid on;set(gca,'linewidth',1.5);
% end of M - file
