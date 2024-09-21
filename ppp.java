public class ppp {  // The class name should match your file name 'Ppp.java'
    
    public static String convertToIpv6(String ipv4Address) {
        String[] octets = ipv4Address.split("\\.");
        if (octets.length != 4) {
            return "Invalid input";
        }

        if (octets[0].equals("127")) {
            return "::1";
        }

        StringBuilder ipv6 = new StringBuilder("::FFFF:");

        try {
            for (int i = 0; i < 4; i++) {
                int octet = Integer.parseInt(octets[i]);
                if (octet < 0 || octet > 255) {
                    return "Invalid input";
                }
                String hex = String.format("%02X", octet);
                ipv6.append(hex);
                if (i == 1) {
                    ipv6.append(":");
                }
            }
        } catch (NumberFormatException e) {
            return "Invalid input";
        }

        return ipv6.toString();
    }

    public static void main(String[] args) {
        System.out.println(convertToIpv6("192.168.0.1"));  // Example usage
    }
}
