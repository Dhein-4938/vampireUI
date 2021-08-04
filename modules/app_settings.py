class Settings():
    # APP SETTINGS
    # ///////////////////////////////////////////////////////////////
    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """
    # CHECKBOX STYLESHEET
    CHECKBOX_STYLESHEET = """
    QCheckBox::indicator {
        border: 3px solid rgb(52, 59, 72);
    	width: 15px;
    	height: 15px;
    	border-radius: 10px;
        background: rgb(44, 49, 60);
    }
    QCheckBox::indicator:hover {
        border: 3px solid rgb(58, 66, 81);
    }
    QCheckBox::indicator:checked {
        background: 3px solid rgb(52, 59, 72);
    	border: 3px solid rgb(52, 59, 72);	
    	background-image: url(:/icons/images/icons/cil-check-alt.png);
    }
    """
    # COMBOBOX STYLESHEET
    COMBOBOX_STYLESHEET = """
    #editor {
        font: 13pt \"Calibri\";
        background-color: rgb(27, 29, 35);
    	border: none;
        padding-bottom: 2px;
        padding-left: 7px;
    }
    #editor::drop-down {
    	subcontrol-origin: padding;
    	subcontrol-position: top right;
    	width: 25px; 
    	border-left-width: 3px;
    	border-left-color: rgba(39, 44, 54, 150);
    	border-left-style: solid;
    	border-top-right-radius: 3px;
    	border-bottom-right-radius: 3px;
    	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);
    	background-position: center;
    	background-repeat: no-reperat;
    }
    #editor QAbstractItemView {
    	color: rgb(255, 121, 198);	
    	background-color: rgb(33, 37, 43);
    	padding: 10px;
    	selection-background-color: rgb(100, 100, 100);
    }
    """
    # SPINBOX STYLESHEET
    SPINBOX_STYLESHEET = """
    #editor {
        font: 12pt \"Calibri\";
        background-color: rgb(39, 44, 54);
        border: none;
    }
    """
    # LINEEDIT STYLESHEET
    LINEEDIT_STYLESHEET = """
    #editor {
        font: 12pt \"Calibri\";
        background-color: rgb(39, 44, 54);
        border: none;
    }
    """

    # TREEVIEW STYLESHEET
    TREEVIEW_STYLESHEET = """
    
    """
    FONT_FAMILY = "sans-serif"
    CHOOSE_FONT_SIZE_ORDER = [   25,    16,    14]
    PARAM_FONT_SIZE_ORDER  = [   14,    13,    11]
    BOLD_ORDER      = [ True,  True, False]
    UNDERLINE_OREDR = [False, False, False]

    SHIFT_DIRECTION = {
        "left-top"      : [  -1,  -1,  -30,   0],
        "left-center"   : [  -1,-0.5,  -30,  12],
        "left-bottom"   : [  -1,   0,  -30,  20],

        "right-top"     : [   0,  -1,  150,   0],
        "right-center"  : [   0,-0.5,  150,  12],
        "right-bottom"  : [   0,   0,  150,  22],
        
        "top-left"      : [  -1,  -1,    0, -20],
        "top-center"    : [-0.5,  -1,   40, -20],
        "top-right"     : [   0,  -1,  100, -20],
        
        "bottom-left"   : [  -1,   0,    0,  35],
        "bottom-center" : [-0.5,   0,   40,  35],
        "bottom-right"  : [   0,   0,  100,  35]
    }

    UNIT_LIST = {
        "unitless" : [""],
        "length"   : ["A","pm","nm","um","mm","cm","m", "in","feet"],
        "energy"   : ["J","eV","meV", "erg", "Ryd", "mRyd", "Ht", "zJ"],
        "moment"   : ["muB","Amm","abAcmcm","J/T","eV/T","erg/G","erg/Oe"],
        "field"    : ["T","mT","uT", "Oe", "kOe"],
        "time"     : ["s","ms","us","ns","ps","fs","as","zs"]
    }

    MATERIAL_SETUP = {
        "Magnetic Properties" : {
            "Damping Constant" :        ["dspin","1"],
            "Atomic Spin Moment" :      ["moment","1.27"],
            "Initial Spin Direction" :  ["dir-1",["random","specific"]],
            "Anisotropy" : {
                "Anisotropy Constant" : ["energy","0"],
                "Type"                : ["combo",["2nd Order Uniaxial","4th Order Uniaxial","6th Order Uniaxial","4th Order Cubic","6th Order Cubic","Neel","Lattice"]],
                "Direction"           : ["dir-2",["random","random grain","specific"]],
                "Lattice Anisotropy File" : ["text"]
            },
            "Relative Gamma" :          ["dspin","1"],
        },
        "Structure Properties" : {
            "Shape" : {
                "Core Shell Size"     : ["dspin","1"],
                "Interface Roughness" : ["dspin","0"],
                "Density"             : ["dspin","1"],
                "Continuous"          : ["none"],
                "Intermixing"         : ["dspin","0"],
                "Geometric File"      : ["text"],
                "Fill Space"          : ["none"]
            },
            "Unit Cell Category"      : ["spin","0"],
            "Height" : {
                "Minimum Height"      : ["dspin","0"],
                "Maximum Height"      : ["dspin","1"]
            },
            "Alloy" : {
                "Type"                : ["combo",["homogeneous","random","granular"]],
                "Scale"               : ["length","50"],
                "Smoothness"          : ["combo dspin",["standard","sharp","smooth","custom"]],
                "Distribution"        : ["combo",["native","reciprocal","homogeneous"]],
                "Fraction"            : ["dspin","0"],
                "Variance"            : ["dspin","0.1"],
                "Save Distribution"   : ["none"],
            },
            "Fill Substructure Space" : ["none"],
            "Voronoi Grain Structure" : ["dspin","0"]
        },
        "Simulation Properties" : {
            "Constrained Angle" : {
                "Theta"               : ["angle"],
                "Phi"                 : ["angle"]
            },
            "Applied Field" : {
                "Strength"            : ["field","0"],
                "Direction"           : ["3dspin","[0.0,0.0,1.0]"]
            },
            "FMR Field" : {
                "Strength"            : ["field","0"],
                "Frequency"           : ["unitless","0"],
                "Direction"           : ["3dspin","[0.0,0.0,1.0]"]
            },
            "Temperature" : {
                "Temperature"                 : ["temp"],
                "Use Phonon Temperature"      : ["none"],
                "Rescaling Exponent"          : ["dspin","1"],
                "Rescaling Curie Temperature" : ["spin","0"]
            }
        },
        "Exchange Properties"         : {
            "Exchange Matrix"         : ["exchange"],
            "DMI Constant"            : ["energy","0"]
        },
        "Spin Properties" : {
            "Slonczewski Spin Torque" : {
                "Adiabatic"           : ["field","0"],
                "Non Adiabatic"       : ["field","0"]
            },
            "Spin Diffusion" : {
                "Spin Diffusion Length"  : ["length","1e3"],
                "Diffusion Constant"     : ["unitless","1e-4"],
                "Spin Accumulation"      : ["unitless","1e8"]
            },
            "Spin Polarisation" : {
                "Spin Polarisation Conductivity" : ["unitless","0.11"],
                "Spin Polarisation Diffusion"    : ["unitless","0.36"]
            },
            "SD Exchange" : {
                "SD Exchange Constant" : ["energy","1.6e-21"]
            }
        }
    }

    MATERIAL_OUTPUT = {
        "Magnetic Properties" : {
            "Damping Constant" :        "damping-constant",
            "Atomic Spin Moment" :      "atomic-spin-moment",
            "Initial Spin Direction" :  "initial-spin-direction",
            "Anisotropy" : {
                "Anisotropy Constant" : None,
                "Type" :            ["second-order-uniaxial-anisotropy-constant","fourth-order-uniaxial-anisotropy-constant","sixth-order-uniaxial-anisotropy-constant","fourth-order-cubic-anisotropy-constant","sixth-order-cubic-anisotropy-constant","neel-anisotropy-constant","lattice-anisotropy-constant"],
                "Direction" :       None,
                "Lattice Anisotropy File" : "lattice-anisotropy-file"
            },
            "Relative Gamma" :          "relative-gamma",
        },
        "Structure Properties" : {
            "Shape" : {
                "Core Shell Size"     : "core-shell-size",
                "Interface Roughness" : "interface-roughness",
                "Density"             : "density",
                "Continuous"          : "continuous",
                "Intermixing"         : "intermixing",
                "Geometric File"      : "geometry-file",
                "Fill Space"          : "fill-space",
            },
            "Unit Cell Category"      : "unit-cell-category",
            "Height" : {
                "Minimum Height"      : "minimum-height",
                "Maximum Height"      : "maximum-height",
            },
            "Alloy" : {
                "Type"                : "host-alloy",
                "Scale"               : "host-alloy-scale",
                "Smoothness"          : "host-alloy-smoothness",
                "Distribution"        : "alloy-distribution",
                "Fraction"            : "alloy-fraction",
                "Variance"            : "alloy-variance",
                "Save Distribution"   : "save-host-alloy-distribution"
            },
            "Fill Substructure Space" : "fill-substructure-space",
            "Voronoi Grain Structure" : "voronoi-grain-substructure-nucleation-height",
        },
        "Simulation Properties" : {
            "Constrained Angle" : {
                "Theta"               : "constraint-angle-theta",   # minimum, maximum, increment(suffix)
                "Phi"                 : "constraint-angle-phi",     # minimum, maximum, increment(suffix)
            },
            "Applied Field" : {
                "Strength"            : "applied-field-strength",
                "Direction"           : "applied-field-unit-vector",
            },
            "FMR Field" : {
                "Strength"            : "fmr-field-strength",
                "Frequency"           : "fmr-field-frequency",
                "Direction"           : "fmr-field-unit-vector",
            },
            "Temperature" : {
                "Temperature"                 : "temperature",      # minimum, maximum (prefix)
                "Use Phonon Temperature"      : "use-phonon-temperature",
                "Rescaling Exponent"          : "temperature-rescaling-exponent",
                "Rescaling Curie Temperature" : "temperature-rescaling-curie-temperature",
            }
        },
        "Exchange Properties"         : {
            "Exchange Matrix"         : "exchange-matrix",
            "DMI Constant"            : "dmi-constant",
        },
        "Spin Properties" : {
            "Slonczewski Spin Torque" : {
                "Adiabatic"           : "slonczewski-adiabatic-spin-torque",
                "Non Adiabatic"       : "slonczewski-non-adiabatic-spin-torque",
            },
            "Spin Diffusion" : {
                "Spin Diffusion Length"  : "spin-diffusion-length",
                "Diffusion Constant"     : "diffusion-constant",
                "Spin Accumulation"      : "spin-accumulation",
            },
            "Spin Polarisation" : {
                "Spin Polarisation Conductivity" : "spin-polarisation-conductivity",
                "Spin Polarisation Diffusion"    : "spin-polarisation-diffusion",
            },
            "SD Exchange" : {
                "SD Exchange Constant" : "sd-exchange-constant"
            }
        }
    }