import os
import io
import zipfile
from datetime import datetime
from flask import Flask, render_template, request, send_file, jsonify, redirect, session
from config import Config
from models import db, Software

# Từ điển dịch tĩnh cho giao diện
TRANSLATIONS = {
    'vi': {
        'title': 'SoftStore PC - Tải Phần Mềm PC Dễ Dàng & Nhanh Chóng',
        'subtitle': 'Mọi liên kết cài đặt đều được dẫn trực tiếp từ trang chủ chính thức, đảm bảo sạch 100% và an toàn tuyệt đối.',
        'search_placeholder': 'Nhập tên phần mềm, công cụ, hoặc nhà phát triển...',
        'search_btn': 'Tìm kiếm',
        'hero_title_1': 'Tải Phần Mềm PC',
        'hero_title_2': 'Dễ Dàng Nhất',
        'hero_subtitle': 'Tìm kiếm ứng dụng bạn cần, bấm nút tải về ngay lập tức. Đơn giản hóa tối đa quá trình cài đặt phần mềm máy tính.',
        'nav_stats': '🚀 Tải phần mềm PC dễ dàng chỉ với 1-Click',
        'download_btn': 'Tải Xuống',
        'download_btn_detail': 'Tải Về Trực Tiếp',
        'connecting': 'Đang kết nối...',
        'downloading': 'Đang tải...',
        'started': 'Đã bắt đầu tải!',
        'size': 'Dung lượng',
        'downloads': 'Lượt tải',
        'tech_info': 'Thông tin kỹ thuật',
        'version': 'Phiên bản',
        'os': 'Hệ điều hành',
        'license': 'Giấy phép',
        'free': 'Miễn phí',
        'select_version': 'Chọn phiên bản tải về:',
        'home': 'Trang chủ',
        'detail_intro': 'Giới thiệu chi tiết',
        'detail_guide': 'Hướng dẫn cài đặt nhanh',
        'detail_guide_p': 'Sau khi nhấn nút tải về, trình duyệt sẽ tự động tải file cài đặt gốc chính thức từ nhà phát triển. Bạn chỉ cần thực hiện:',
        'detail_step1': 'Nhấp vào tệp tin tải về (.exe hoặc .msi) ở thanh công cụ tải xuống của trình duyệt.',
        'detail_step2': 'Chọn <strong>Yes</strong> hoặc <strong>Run</strong> nếu hệ thống bảo mật Windows SmartScreen hiển thị cảnh báo.',
        'detail_step3': 'Tiến hành làm theo các bước cài đặt mặc định trên màn hình (nhấn Next &rsaquo; Finish) để hoàn tất.',
        'empty_state_title': 'Không tìm thấy phần mềm nào',
        'empty_state_desc': 'Chúng tôi không tìm thấy kết quả phù hợp với từ khóa của bạn. Vui lòng kiểm tra lại chính tả hoặc thử tìm kiếm từ khác.',
        'empty_state_desc_query': 'Chúng tôi không tìm thấy kết quả phù hợp với từ khóa "{query}" của bạn. Bạn hãy kiểm tra lại chính tả hoặc thử bộ lọc danh mục khác.',
        'empty_state_btn': 'Quay lại trang chủ',
        'similar_apps': 'Các phần mềm tương tự',
        'copyright': '© 2026 SoftStore PC. Kho phần mềm máy tính tải xuống dễ dàng và nhanh chóng.',
        'developer_label': 'Phát triển bởi',
        'error_404_title': 'Không tìm thấy trang - SoftStore PC',
        'error_404_h2': 'Lỗi 404: Không Tìm Thấy Trang',
        'error_404_desc': 'Đường dẫn bạn truy cập có thể đã bị thay đổi hoặc không tồn tại trên hệ thống của chúng tôi.',
        'error_500_title': 'Lỗi hệ thống - SoftStore PC',
        'error_500_h2': 'Lỗi 500: Sự cố kết nối máy chủ',
        'error_500_desc': 'Đã xảy ra lỗi hệ thống đột ngột phía máy chủ. Xin vui lòng thử lại sau.',
        'categories': {
            'all': 'Tất cả ứng dụng',
            'browsers': 'Trình duyệt Web',
            'dev': 'Lập trình & IDE',
            'design': 'Đồ họa & Thiết kế',
            'utilities': 'Tiện ích hệ thống',
            'games': 'Trò chơi & Kết nối',
            'security': 'Bảo mật & Diệt virus',
            'office': 'Văn phòng & Soạn thảo',
            'os_iso': 'Hệ điều hành & ISO'
        }
    },
    'en': {
        'title': 'SoftStore PC - Easy & Fast PC Software Downloads',
        'subtitle': 'All installation links are sourced directly from the official homepage, ensuring 100% clean and absolute safety.',
        'search_placeholder': 'Enter software name, tools, or developer...',
        'search_btn': 'Search',
        'hero_title_1': 'Download PC Software',
        'hero_title_2': 'The Easiest Way',
        'hero_subtitle': 'Find the application you need, click the download button instantly. Maximize simplicity for computer software installation.',
        'nav_stats': '🚀 Download PC software easily with 1-Click',
        'download_btn': 'Download',
        'download_btn_detail': 'Direct Download',
        'connecting': 'Connecting...',
        'downloading': 'Downloading...',
        'started': 'Download started!',
        'size': 'File Size',
        'downloads': 'Downloads',
        'tech_info': 'Technical Info',
        'version': 'Version',
        'os': 'OS Support',
        'license': 'License',
        'free': 'Free',
        'select_version': 'Select version to download:',
        'home': 'Home',
        'detail_intro': 'Detailed Introduction',
        'detail_guide': 'Quick Installation Guide',
        'detail_guide_p': 'After clicking the download button, your browser will automatically download the official original installation file from the developer. You only need to do:',
        'detail_step1': 'Click on the downloaded file (.exe or .msi) in the browser\'s download toolbar.',
        'detail_step2': 'Select <strong>Yes</strong> or <strong>Run</strong> if the Windows SmartScreen security system displays a warning.',
        'detail_step3': 'Proceed by following the default installation steps on the screen (click Next &rsaquo; Finish) to complete.',
        'empty_state_title': 'No software found',
        'empty_state_desc': 'We could not find any results matching your keyword. Please check your spelling or try another search term.',
        'empty_state_desc_query': 'We could not find any results matching your keyword "{query}". Please check your spelling or try another category filter.',
        'empty_state_btn': 'Back to homepage',
        'similar_apps': 'Similar Software',
        'copyright': '© 2026 SoftStore PC. Computer software library downloaded easily and quickly.',
        'developer_label': 'Developed by',
        'error_404_title': 'Page Not Found - SoftStore PC',
        'error_404_h2': 'Error 404: Page Not Found',
        'error_404_desc': 'The link you accessed may have been changed or does not exist on our system.',
        'error_500_title': 'System Error - SoftStore PC',
        'error_500_h2': 'Error 500: Server Connection Issue',
        'error_500_desc': 'An unexpected server-side error occurred. Please try again later.',
        'categories': {
            'all': 'All Apps',
            'browsers': 'Web Browsers',
            'dev': 'Programming & IDE',
            'design': 'Graphics & Design',
            'utilities': 'System Utilities',
            'games': 'Gaming & Social',
            'security': 'Security & Antivirus',
            'office': 'Office & Editing',
            'os_iso': 'OS & ISO Files'
        }
    }
}

# Bản dịch tiếng Anh cho mô tả và mô tả chi tiết của từng phần mềm cụ thể
SOFTWARE_TRANSLATIONS = {
    'chrome': {
        'description': 'The world\'s fastest, safest, and easiest-to-use web browser developed by Google.',
        'detail_description': 'Google Chrome is a free web browser used by billions of people thanks to its extremely fast page loading speed, built-in advanced security tools, and a huge store of extensions supporting all work and study needs.'
    },
    'firefox': {
        'description': 'Open-source web browser, protecting user privacy to the maximum.',
        'detail_description': 'Mozilla Firefox is a famous open-source browser committed to maximum privacy protection for users. Smart tracking protection, low RAM consumption, and flexible interface customization.'
    },
    'brave': {
        'description': 'Security-focused web browser, blocking ads automatically and speeding up web browsing.',
        'detail_description': 'Brave Browser automatically blocks ads and online trackers, helping pages load up to 3 times faster, saving battery and bandwidth. It also integrates advanced security features and a secure Web3 wallet.'
    },
    'vscode': {
        'description': 'Lightweight but most powerful source code editor for programmers.',
        'detail_description': 'Visual Studio Code (VS Code) is a free source code editor running on Windows, macOS, and Linux. Built-in Git, supports visual debugging, and a rich plugin store supporting writing HTML, JS, Python, C++, etc.'
    },
    'python': {
        'description': 'Official Python programming language installer and interpreter.',
        'detail_description': 'Python is a versatile, easy-to-learn, and extremely powerful programming language widely used in AI, data analysis, and web development. The installer contains the Python interpreter, standard libraries, and the pip package manager.'
    },
    'git': {
        'description': 'Free distributed version control system for software projects.',
        'detail_description': 'Git is the industry standard for source code management and tracking change history of projects. Supports effective teamwork, smart branching, and absolute compatibility with GitHub, GitLab.'
    },
    'xampp': {
        'description': 'Extremely popular PHP development environment integrated with Apache, MariaDB, PHP, and Perl.',
        'detail_description': 'XAMPP is the perfect toolset helping web developers build local web servers easily and quickly with just one click. Suitable for programming and testing PHP source code.'
    },
    'visualstudio': {
        'description': 'The most comprehensive and professional integrated development environment (IDE) from Microsoft.',
        'detail_description': 'Microsoft Visual Studio is an extremely powerful IDE for developing Windows (.NET, C++), web, cloud, and mobile applications. Suitable for large enterprise projects from Microsoft.'
    },
    'cursor-editor': {
        'description': 'The most advanced AI-integrated source code editor today, built on VS Code.',
        'detail_description': 'Cursor is a next-generation AI programming IDE deeply optimized to help programmers write code many times faster. Supports smart auto-completion, bug fixing, code explanation, and direct chat with advanced AI models like Claude 3.5 Sonnet and GPT-4o.'
    },
    'docker': {
        'description': 'Tool for packaging, managing, and running applications in isolated containers.',
        'detail_description': 'Docker Desktop provides a complete environment to build, share, and run containerized applications on Windows. Integrated Kubernetes, Docker Engine, and intuitive GUI.'
    },
    'nodejs': {
        'description': 'JavaScript server-side runtime environment built on the V8 engine.',
        'detail_description': 'Node.js allows programmers to run JavaScript code outside the browser to build high-speed network applications, API servers, and realtime applications.'
    },
    'intellij': {
        'description': 'Leading IDE for Java, Kotlin programming, and enterprise software development.',
        'detail_description': 'IntelliJ IDEA is the smartest integrated development environment (IDE) for Java and Kotlin. Supports code refactoring, smart syntax analysis, and built-in popular build tools like Maven and Gradle.'
    },
    'antigravity-agent': {
        'description': 'The world\'s most advanced automated AI programming agent, optimized code and 1-Click bug fixing.',
        'detail_description': 'Antigravity AI Agent is a next-generation automated programming system developed by Google DeepMind. The Agent can explore codebases, edit complex files, fix compilation errors, and design top UX/UI according to industry standards with a single prompt.'
    },
    'blender': {
        'description': 'Open-source 3D graphics design, animation, and video editing software.',
        'detail_description': 'Blender is a completely free and open-source 3D content creation suite. It supports the entire modeling pipeline: modeling, rigging, animation, physics simulation, video rendering, and post-production.'
    },
    'gimp': {
        'description': 'Professional image editing software, a free Photoshop alternative.',
        'detail_description': 'GIMP (GNU Image Manipulation Program) is a free raster graphics editor. It is used for image retouching, free-form drawing, image format conversion, and specialized tasks equivalent to Adobe Photoshop.'
    },
    'vlc': {
        'description': 'Free media player, opens almost all video and music formats.',
        'detail_description': 'VLC Media Player is a free, open-source, cross-platform multimedia player. It can play most multimedia files as well as DVDs, Audio CDs, VCDs, and streaming protocols without installing additional codecs.'
    },
    'winrar': {
        'description': 'World\'s leading powerful RAR and ZIP file compression and decompression software.',
        'detail_description': 'WinRAR is an extremely powerful archiving tool that helps compress and decompress data quickly. It can backup your data, reduce email attachment sizes, decompress RAR, ZIP, and other files downloaded from the Internet.'
    },
    'ccleaner': {
        'description': 'System junk cleaner, registry fixer, and computer speed optimizer utility.',
        'detail_description': 'CCleaner is the leading cleaning tool that protects your privacy and makes your computer faster and safer. The software will remove junk files, browsing history, and temporary files, freeing up hard drive space.'
    },
    'vmware': {
        'description': 'Most powerful computer virtualization software, running multiple operating systems simultaneously.',
        'detail_description': 'VMware Workstation allows IT professionals and developers to run multiple virtual machines on the same Windows operating system. Create independent environments to test applications safely.'
    },
    'virtualbox': {
        'description': 'Free open-source virtualization software, supporting emulation of multiple operating systems on the computer.',
        'detail_description': 'Oracle VM VirtualBox is a powerful free and open-source virtualization software that allows users to test other operating systems (Linux, Windows, macOS...) right on the current computer without affecting the main system.'
    },
    'steam': {
        'description': 'The world\'s largest online copyrighted game distribution platform.',
        'detail_description': 'Steam is the ultimate destination to play, discuss, and create games. Featuring tens of thousands of copyrighted games, automatic updates, and an active global player community.'
    },
    'discord': {
        'description': 'Voice, video, and text chat application designed for gamers.',
        'detail_description': 'Discord is the easiest way to talk over voice, video, and text. The software allows you to create private chat channels, and share game screens smoothly with friends completely free.'
    },
    'teamviewer': {
        'description': 'The world\'s number one remote desktop connection and support control solution.',
        'detail_description': 'TeamViewer helps you connect and control remote computer screens anywhere. Supports file transfer and online chat, extremely convenient for office and technical work.'
    },
    'ultraviewer': {
        'description': 'Ultra-lightweight, free, and popular remote desktop control software in Vietnam.',
        'detail_description': 'UltraViewer helps you control client computers remotely to support software quickly. Simple interface, absolutely secure with a mechanism to generate random passwords for each session.'
    },
    'malwarebytes': {
        'description': 'Powerful malware, trojan, and ransomware scanning and removal software.',
        'detail_description': 'Malwarebytes is a next-generation antivirus and malware software, protecting your computer against spyware, malicious adware, and hackers using a smart real-time behavior detection system.'
    },
    'notepadpp': {
        'description': 'Versatile, ultra-lightweight text and source code editor for Windows.',
        'detail_description': 'Notepad++ is a free text editor that perfectly replaces Windows Notepad. It supports syntax highlighting for multiple programming languages, opening multiple tabs at once, and is extremely lightweight.'
    },
    'unikey': {
        'description': 'The best, most lightweight, and popular Vietnamese input method on Windows.',
        'detail_description': 'UniKey is the most popular free open-source Vietnamese keyboard software in Vietnam. It supports common Vietnamese character sets (Unicode, VNI, TCVN3...) and very accurate Telex and VNI input methods.'
    },
    'zoom': {
        'description': 'Leading application for organizing online workshops, learning, and meetings.',
        'detail_description': 'Zoom Meetings provides online meetings and HD video conferencing solutions, sharing documents conveniently, supporting easy remote work and study.'
    },
    'windows-11': {
        'description': 'Official Microsoft Windows 11 Enterprise installation ISO file.',
        'detail_description': 'Official ISO installation of Windows 11 Enterprise (23H2). Integrated advanced security features, Copilot AI, and a modern rounded-corner design interface.'
    },
    'windows-10': {
        'description': 'The most stable and popular Windows 10 Enterprise installation ISO file.',
        'detail_description': 'Official ISO installation of Windows 10 Enterprise (22H2). Perfect for all personal and business computers with optimal performance and best software compatibility.'
    },
    'windows-7': {
        'description': 'The legendary Windows 7 Ultimate SP1 64-bit installation ISO file.',
        'detail_description': 'Original clean, extremely lightweight, and stable Windows 7 SP1 Ultimate 64-bit/32-bit operating system. A great choice for old computer configurations or installing as virtual machines for testing.'
    },
    'ubuntu': {
        'description': 'The most popular and user-friendly Linux open-source operating system today.',
        'detail_description': 'Ubuntu Desktop 24.04.4 LTS (Noble Numbat) brings an intuitive, modern workspace, built-in browser, LibreOffice office suite, and a huge, extremely secure app store.'
    },
    'kali-linux': {
        'description': 'Ultimate Linux distribution for security penetration testing and ethical hacking.',
        'detail_description': 'Kali Linux is a Debian-based open-source operating system pre-configured with hundreds of specialized tools for penetration testing, malware analysis, information recovery, and network security.'
    }
}

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    @app.context_processor
    def inject_globals():
        lang = session.get('lang', 'vi')
        
        # Hàm dịch tĩnh
        def translate(key, **kwargs):
            keys = key.split('.')
            val = TRANSLATIONS.get(lang, TRANSLATIONS['vi'])
            for k in keys:
                if isinstance(val, dict):
                    val = val.get(k, '')
                else:
                    val = ''
                    break
            if not val:
                return key
            if kwargs:
                return val.format(**kwargs)
            return val
            
        # Hàm dịch thông tin phần mềm động
        def translate_sw(sw, field):
            val = getattr(sw, field, '')
            if lang == 'en':
                sw_trans = SOFTWARE_TRANSLATIONS.get(sw.slug, {})
                if field in sw_trans:
                     return sw_trans[field]
            return val

        # Lấy danh mục được dịch
        localized_categories = TRANSLATIONS[lang]['categories']

        return dict(
            t=translate,
            t_sw=translate_sw,
            current_lang=lang,
            CATEGORIES=localized_categories
        )
        
    @app.route('/')
    def index():
        lang = session.get('lang', 'vi')
        localized_categories = TRANSLATIONS[lang]['categories']
        category = request.args.get('category', 'all').strip()
        search_query = request.args.get('q', '').strip()
        
        query = Software.query
        
        # Lọc theo danh mục
        if category != 'all' and category in localized_categories:
            query = query.filter_by(category=category)
            
        # Tìm kiếm theo tên hoặc nhà phát triển
        if search_query:
            query = query.filter(
                (Software.name.like(f'%{search_query}%')) | 
                (Software.developer.like(f'%{search_query}%')) | 
                (Software.description.like(f'%{search_query}%'))
            )
            
        softwares = query.order_by(Software.download_count.desc()).all()
        return render_template('index.html', softwares=softwares, selected_category=category, search_query=search_query)

    @app.route('/app/<slug>')
    def detail(slug):
        software = Software.query.filter_by(slug=slug).first_or_404()
        
        # Lấy thêm các phần mềm gợi ý cùng danh mục
        related = Software.query.filter(Software.category == software.category, Software.id != software.id).limit(4).all()
        return render_template('detail.html', software=software, related=related)

    @app.route('/download/<slug>')
    def download(slug):
        software = Software.query.filter_by(slug=slug).first_or_404()
        
        # Lấy phiên bản được chọn từ tham số query v
        selected_version = request.args.get('v', '').strip()
        download_url = None
        
        if selected_version:
            from models import SoftwareVersion
            ver = SoftwareVersion.query.filter_by(software_id=software.id, version=selected_version).first()
            if ver:
                download_url = ver.download_url
                
        if not download_url:
            download_url = software.download_url
            
        # Tăng số lượt tải thực tế
        software.download_count += 1
        db.session.commit()
        
        # Chuyển hướng trực tiếp tới tệp tin exe/msi chính thức
        return redirect(download_url)

    @app.route('/change-lang/<lang>')
    def change_lang(lang):
        if lang in ['vi', 'en']:
            session['lang'] = lang
        # Chuyển hướng về trang trước đó, hoặc trang chủ nếu không có
        return redirect(request.referrer or '/')

    @app.route('/api/download-count/<int:app_id>', methods=['POST'])
    def increment_count(app_id):
        software = Software.query.get_or_404(app_id)
        software.download_count += 1
        db.session.commit()
        return jsonify({'success': True, 'new_count': software.download_count})

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
        
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    # Khởi tạo bảng dữ liệu và tự động seed nếu trống
    with app.app_context():
        db.create_all()
        try:
            if Software.query.first() is None:
                from init_db import seed_database
                # Seed dữ liệu mà không xóa bảng (drop_tables=False)
                seed_database(app, drop_tables=False)
                print("Tự động seed dữ liệu thành công trên môi trường mới!")
        except Exception as e:
            print(f"Lỗi kiểm tra/seed dữ liệu tự động: {e}")
        
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
