using System;
using System.Threading;

namespace main
{



	/// <summary>
	/// @version 1.0
	/// @author Asutosh
	/// </summary>
	public class WebLogin : JFrame
	{

		private web webr;
		private Thread th;

		public WebLogin()
		{
			initComponents();
		}

		internal TrayIcon trayIcon;
		internal SystemTray tray;
		public virtual void setHideToSystemTray()
		{
			Console.WriteLine("setting up systemtray");

			if (SystemTray.Supported)
			{
				Console.WriteLine("system tray supported");
				tray = SystemTray.SystemTray;

				Image image = Toolkit.DefaultToolkit.getImage("wifi.png");
				ActionListener exitListener = new ActionListenerAnonymousInnerClassHelper(this);
				PopupMenu popup = new PopupMenu();
				MenuItem defaultItem = new MenuItem("Exit");
				defaultItem.addActionListener(exitListener);
				popup.add(defaultItem);
				defaultItem = new MenuItem("Open");
				defaultItem.addActionListener(new ActionListenerAnonymousInnerClassHelper2(this));
				popup.add(defaultItem);
				trayIcon = new TrayIcon(image, "Wifi WebLogin", popup);
				trayIcon.ImageAutoSize = true;
			}
			else
			{
				Console.WriteLine("system tray not supported");
			}

			trayIcon.addMouseListener(new MouseListenerAnonymousInnerClassHelper(this));
			addWindowStateListener(new WindowStateListenerAnonymousInnerClassHelper(this));
			IconImage = Toolkit.DefaultToolkit.getImage("wifi.png");


		}

		private class ActionListenerAnonymousInnerClassHelper : ActionListener
		{
			private readonly WebLogin outerInstance;

			public ActionListenerAnonymousInnerClassHelper(WebLogin outerInstance)
			{
				this.outerInstance = outerInstance;
			}

			public virtual void actionPerformed(ActionEvent e)
			{
				Console.WriteLine("Exiting....");
				Environment.Exit(0);
			}
		}

		private class ActionListenerAnonymousInnerClassHelper2 : ActionListener
		{
			private readonly WebLogin outerInstance;

			public ActionListenerAnonymousInnerClassHelper2(WebLogin outerInstance)
			{
				this.outerInstance = outerInstance;
			}

			public virtual void actionPerformed(ActionEvent e)
			{
				Visible = true;
				ExtendedState = JFrame.NORMAL;
			}
		}

		private class MouseListenerAnonymousInnerClassHelper : MouseListener
		{
			private readonly WebLogin outerInstance;

			public MouseListenerAnonymousInnerClassHelper(WebLogin outerInstance)
			{
				this.outerInstance = outerInstance;
			}


			public override void mouseReleased(MouseEvent e)
			{
				// TODO Auto-generated method stub

			}

			public override void mousePressed(MouseEvent e)
			{
				// TODO Auto-generated method stub

			}

			public override void mouseExited(MouseEvent e)
			{
				// TODO Auto-generated method stub

			}

			public override void mouseEntered(MouseEvent e)
			{
				// TODO Auto-generated method stub

			}

			public override void mouseClicked(MouseEvent arg0)
			{
				// TODO Auto-generated method stub
				Visible = true;
				ExtendedState = JFrame.NORMAL;
			}
		}

		private class WindowStateListenerAnonymousInnerClassHelper : WindowStateListener
		{
			private readonly WebLogin outerInstance;

			public WindowStateListenerAnonymousInnerClassHelper(WebLogin outerInstance)
			{
				this.outerInstance = outerInstance;
			}

			public virtual void windowStateChanged(WindowEvent e)
			{
				if (e.NewState == ICONIFIED)
				{
					try
					{
						outerInstance.tray.add(outerInstance.trayIcon);
						Visible = false;
						Console.WriteLine("added to SystemTray");
					}
					catch (AWTException)
					{
						Console.WriteLine("unable to add to tray");
					}
				}
				if (e.NewState == 7)
				{
					try
					{
						outerInstance.tray.add(outerInstance.trayIcon);
						Visible = false;
						Console.WriteLine("added to SystemTray");
					}
					catch (AWTException)
					{
						Console.WriteLine("unable to add to system tray");
					}
				}
				if (e.NewState == MAXIMIZED_BOTH)
				{
					outerInstance.tray.remove(outerInstance.trayIcon);
					Visible = true;
					Console.WriteLine("Tray icon removed");
				}
				if (e.NewState == NORMAL)
				{
					outerInstance.tray.remove(outerInstance.trayIcon);
					Visible = true;
					Console.WriteLine("Tray icon removed");
				}
			}
		}



//JAVA TO C# CONVERTER TODO TASK: Most Java annotations will not have direct .NET equivalent attributes:
//ORIGINAL LINE: @SuppressWarnings("unchecked") private void initComponents()
		private void initComponents()
		{

			jLabel1 = new javax.swing.JLabel();
			jLabel2 = new javax.swing.JLabel();
			jTextField1 = new javax.swing.JTextField();
			jLabel3 = new javax.swing.JLabel();
			jTextField2 = new javax.swing.JTextField();
			jButton1 = new javax.swing.JButton();
			jButton2 = new javax.swing.JButton();
			jButton3 = new javax.swing.JButton();
			jButton4 = new javax.swing.JButton();
			jLabel4 = new javax.swing.JLabel();
			jLabel5 = new javax.swing.JLabel();
			jTextField3 = new javax.swing.JTextField();
			jTextField4 = new javax.swing.JTextField();
			webr = new web(this);
			th = webr;
			th.Start();

			DefaultCloseOperation = javax.swing.WindowConstants.EXIT_ON_CLOSE;


			jTextField1.Editable = false;
			jTextField2.Editable = false;
			jTextField3.Text = webr.username;
			jTextField4.Text = webr.password;

			jLabel1.Font = new java.awt.Font("Tahoma", 0, 18); // NOI18N
			jLabel1.Text = "Rajendra Wifi Login";

			jLabel2.Text = "Internet Status";

			jLabel3.Text = "Program Status";

			jButton1.Text = "Pause";
			jButton1.addActionListener(new ActionListenerAnonymousInnerClassHelper3(this));

			jButton2.Text = "Start";
			jButton2.Enabled = false;
			jButton2.addActionListener(new ActionListenerAnonymousInnerClassHelper4(this));


			jButton3.Text = "Close";
			jButton3.addActionListener(new ActionListenerAnonymousInnerClassHelper5(this));

			jButton4.Text = "Change";
			jButton4.addActionListener(new ActionListenerAnonymousInnerClassHelper6(this));

			jLabel4.Text = "User Name";

			jLabel5.Text = "Password";

			setHideToSystemTray();

			javax.swing.GroupLayout layout = new javax.swing.GroupLayout(ContentPane);
			ContentPane.Layout = layout;
			layout.HorizontalGroup = layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGap(112, 112, 112).addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 163, javax.swing.GroupLayout.PREFERRED_SIZE)).addGroup(layout.createSequentialGroup().addGap(46, 46, 46).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING).addComponent(jButton1).addComponent(jLabel2).addComponent(jLabel3).addComponent(jLabel4).addComponent(jLabel5)).addGap(29, 29, 29).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false).addGroup(layout.createSequentialGroup().addComponent(jButton2).addGap(18, 18, 18).addComponent(jButton3)).addComponent(jTextField1).addComponent(jTextField4).addComponent(jTextField3).addComponent(jTextField2)).addGap(18, 18, 18).addComponent(jButton4))).addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, short.MaxValue));
			layout.VerticalGroup = layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGap(28, 28, 28).addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 55, javax.swing.GroupLayout.PREFERRED_SIZE).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addComponent(jLabel2).addComponent(jTextField1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addGap(18, 18, 18).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(jLabel3).addComponent(jTextField2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addGap(18, 18, 18).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING).addGroup(layout.createSequentialGroup().addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(jLabel4).addComponent(jTextField3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(jLabel5).addComponent(jTextField4, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)).addGap(40, 40, 40)).addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup().addComponent(jButton4).addGap(53, 53, 53))).addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE).addComponent(jButton1).addComponent(jButton2).addComponent(jButton3)).addContainerGap(53, short.MaxValue));


			pack();
		}

		private class ActionListenerAnonymousInnerClassHelper3 : ActionListener
		{
			private readonly WebLogin outerInstance;

			public ActionListenerAnonymousInnerClassHelper3(WebLogin outerInstance)
			{
				this.outerInstance = outerInstance;
			}


			public override void actionPerformed(ActionEvent e)
			{

				outerInstance.webr.Suspend();
				//webr.run = false;


				outerInstance.webr.istatus = "";
				outerInstance.webr.pstatus = "paused";
				outerInstance.update();
				outerInstance.jButton1.Enabled = false;
				outerInstance.jButton2.Enabled = true;

			}
		}

		private class ActionListenerAnonymousInnerClassHelper4 : ActionListener
		{
			private readonly WebLogin outerInstance;

			public ActionListenerAnonymousInnerClassHelper4(WebLogin outerInstance)
			{
				this.outerInstance = outerInstance;
			}


			public override void actionPerformed(ActionEvent e)
			{
				// TODO Auto-generated method stub
				outerInstance.webr.run_Renamed = true;
				outerInstance.webr.Resume();
				outerInstance.jButton2.Enabled = false;
				outerInstance.jButton1.Enabled = true;

			}
		}

		private class ActionListenerAnonymousInnerClassHelper5 : ActionListener
		{
			private readonly WebLogin outerInstance;

			public ActionListenerAnonymousInnerClassHelper5(WebLogin outerInstance)
			{
				this.outerInstance = outerInstance;
			}


			public override void actionPerformed(ActionEvent e)
			{

				outerInstance.webr.run_Renamed = false;
				outerInstance.th.Abort();
				outerInstance.Visible = false;
				outerInstance.dispose();
				Environment.Exit(0);

			}
		}

		private class ActionListenerAnonymousInnerClassHelper6 : ActionListener
		{
			private readonly WebLogin outerInstance;

			public ActionListenerAnonymousInnerClassHelper6(WebLogin outerInstance)
			{
				this.outerInstance = outerInstance;
			}


			public override void actionPerformed(ActionEvent e)
			{

				outerInstance.webr.password = outerInstance.jTextField4.Text;
				outerInstance.webr.username = outerInstance.jTextField3.Text;
				outerInstance.jTextField3.Text = outerInstance.webr.username;
				outerInstance.jTextField4.Text = outerInstance.webr.password;

			}
		}



		public virtual void update()
		{
				jTextField2.Text = webr.pstatus;
				jTextField1.Text = webr.istatus;


		}

		public static void Main(string[] args)
		{

			   try
			   {
					foreach (UIManager.LookAndFeelInfo info in UIManager.InstalledLookAndFeels)
					{
						if ("Nimbus".Equals(info.Name))
						{
							UIManager.LookAndFeel = info.ClassName;
							break;
						}
					}
			   }
				catch (ClassNotFoundException ex)
				{
//JAVA TO C# CONVERTER WARNING: The .NET Type.FullName property will not always yield results identical to the Java Class.getName method:
					java.util.logging.Logger.getLogger(typeof(WebLogin).FullName).log(java.util.logging.Level.SEVERE, null, ex);
				}
				catch (InstantiationException ex)
				{
//JAVA TO C# CONVERTER WARNING: The .NET Type.FullName property will not always yield results identical to the Java Class.getName method:
					java.util.logging.Logger.getLogger(typeof(WebLogin).FullName).log(java.util.logging.Level.SEVERE, null, ex);
				}
				catch (IllegalAccessException ex)
				{
//JAVA TO C# CONVERTER WARNING: The .NET Type.FullName property will not always yield results identical to the Java Class.getName method:
					java.util.logging.Logger.getLogger(typeof(WebLogin).FullName).log(java.util.logging.Level.SEVERE, null, ex);
				}
				catch (javax.swing.UnsupportedLookAndFeelException ex)
				{
//JAVA TO C# CONVERTER WARNING: The .NET Type.FullName property will not always yield results identical to the Java Class.getName method:
					java.util.logging.Logger.getLogger(typeof(WebLogin).FullName).log(java.util.logging.Level.SEVERE, null, ex);
				}
				//</editor-fold>

				/* Create and display the form */
				java.awt.EventQueue.invokeLater(() =>
				{
					(new WebLogin()).Visible = true;
				});
		}


		// Variables declaration - do not modify                     
		private javax.swing.JButton jButton1;
		private javax.swing.JButton jButton2;
		private javax.swing.JButton jButton3;
		private javax.swing.JButton jButton4;
		private javax.swing.JLabel jLabel1;
		private javax.swing.JLabel jLabel2;
		private javax.swing.JLabel jLabel3;
		private javax.swing.JLabel jLabel4;
		private javax.swing.JLabel jLabel5;
		private javax.swing.JTextField jTextField1;
		private javax.swing.JTextField jTextField2;
		private javax.swing.JTextField jTextField3;
		private javax.swing.JTextField jTextField4;
		// End of variables declaration                   
	}

}